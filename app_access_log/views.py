from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from celery.result import AsyncResult
import datetime

from .tasks import get_datetime


@csrf_exempt
def get_time(requests):

    resp = get_datetime.delay()
    task_id = resp.id

    return JsonResponse({'task_id': task_id}, safe=False)
