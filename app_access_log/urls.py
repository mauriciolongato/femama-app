from django.urls import path, include
from .views import get_time


app_name = 'app_access_log'


urlpatterns = [
    path('get_time/', get_time, name='get_time'),
    ]
