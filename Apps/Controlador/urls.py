from django.urls import path
from .views import *

urlpatterns = [
    path('Index/', IndexView.as_view()),
]