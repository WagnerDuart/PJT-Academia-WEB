from django.urls import path
from academia.views import home

urlpatterns = [
    path('', home),
]
