from django.urls import path, include
from app import views

urlpatterns = [
    path('api/', views.api_view, name='api_view'),
]
