from django.urls import path
from . import views
from .views import *


app_name = 'wordcount'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file.html'),
    path('wordcount/<str:word>/', views.word_count, name='word_count'),
    path('clear/', views.clear_memory, name='clear_memory.html'),
] 