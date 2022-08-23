
import datetime
import time
import pytz
import requests
from dotenv import load_dotenv
from django.utils import timezone

from .models import Mailing, Client, Message
from django_rq import job
import logging
import os


load_dotenv()

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")

logger = logging.getLogger(__name__)


@job
def send_message(data, mailing_id, url=URL, token=TOKEN):
    mail = Mailing.objects.get(pk=mailing_id)
    now = timezone.now()

    if mail.date_start <= now <= mail.date_end:
        header = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'}
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            logger.error(f"Message id: {data['id']}, error occurred")
        else:
            logger.info(f"Message id: {data['id']}, Sending status: 'Sent'")
            Message.objects.filter(pk=data['id']).update(sending_status='Sent', sending_time=now)
    else:
        logger.info(f"Message id: {data['id']}, "
                    f"The current time is not for sending the message")

