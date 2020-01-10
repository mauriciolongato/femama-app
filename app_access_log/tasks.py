from celery import shared_task
import datetime
import time


@shared_task
def get_datetime():
    time.sleep(2)
    return datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
