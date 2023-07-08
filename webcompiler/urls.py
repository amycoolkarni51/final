from django.urls import path
from . import views

urlpatterns = [
    path('editor/', views.home),
    path('preview/', views.preview)
]