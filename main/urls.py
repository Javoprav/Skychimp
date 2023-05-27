from django.contrib import admin
from django.urls import path, include
from main.apps import MainConfig
from main.views import CustomerListView

app_name = MainConfig.name


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
]
