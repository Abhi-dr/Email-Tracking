from django.urls import path
from .views import send_email, track_mail

urlpatterns = [
    path('send_email', send_email, name='send_email'),
    path('track_mail/<str:uuid>/<str:recipient>/', track_mail, name='track_mail'),
]
