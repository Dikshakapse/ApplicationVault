# core/tasks.py

from celery import shared_task
from utils.telegram import send_telegram_message

@shared_task
def send_telegram_message_async(message):
    send_telegram_message(message)
