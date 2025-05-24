from django.urls import path
from . import views

urlpatterns = [
    path('', views.partner_form, name='partner_form'),
    path('success/', views.partner_success, name='partner_success'),
]