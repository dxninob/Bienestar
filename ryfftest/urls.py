from django.urls import path
from . import views

urlpatterns = [
  path('ryfftest/', views.ryfftest),
]