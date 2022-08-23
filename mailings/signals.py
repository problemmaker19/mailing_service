import logging
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from rq import Queue
from redis import Redis
from django.utils import timezone
from .models import Mailing, Client, Message
from .jobs import send_message


logger = logging.getLogger(__name__)


@receiver(post_save, sender=Mailing, dispatch_uid="create_message")
def create_message(sender, instance, created, **kwargs):

    redis = Redis()
    q = Queue(name='default', connection=redis)

    if created:
        mailing = Mailing.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(Q(mobile_operator_code=mailing.mobile_operator_code) |
                                        Q(tag=mailing.tag)).all()

        for client in clients:
            Message.objects.create(
                sending_status="No sent",
                client_id=client.id,
                mailing_id=instance.id
            )
            message = Message.objects.filter(mailing_id=instance.id, client_id=client.id).first()
            data = {
                'id': message.id,
                "phone": client.phone_number,
                "text": mailing.text
            }
            mailing_id = mailing.id

            if instance.missed_time_to_send:
                logger.error("You missed time to schedule this mailing")
            else:
                q.enqueue_at(mailing.date_start, send_message, data=data, mailing_id=mailing_id,)
