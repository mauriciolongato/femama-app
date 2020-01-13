from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import dashboard_frame, update_dados_form, \
    update_dados_score, mapa_br, update_dropdown_metabase, user_logout


app_name = 'dashboard'


urlpatterns = [
    path('info/', dashboard_frame, name='dash'),
    path('info/<str:dashname>/', dashboard_frame),
    path('update_dados_censo/', update_dados_form),
    path('update_dados_score/', update_dados_score),
    path('update_dropdowns/', update_dropdown_metabase),
    path('mapa_br/', mapa_br, name='mapa_br'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/logout/', user_logout)
    ]
