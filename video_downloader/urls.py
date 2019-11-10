from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('details/<str:youtube_url>/', views.video_details),
    path('stream/<str:youtube_url>/<str:extension>/<str:resolution>/', views.video_stream_details)
]
