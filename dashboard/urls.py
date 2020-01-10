from django.urls import path, include
from .views import dashboard_frame, update_dados_form, update_dados_score, mapa_br


app_name = 'dashboard'


urlpatterns = [
    path('info/', dashboard_frame, name='url_dashboard'),
    path('update_dados_censo/', update_dados_form, name='form'),
    path('update_dados_score/', update_dados_score, name='form'),
    path('mapa_br/', mapa_br, name='mapa_br'),
    ]
