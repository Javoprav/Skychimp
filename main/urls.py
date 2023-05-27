from django.contrib import admin
from django.urls import path, include
from main.apps import MainConfig
from main.views import CustomerListView, CustomerDetailView

app_name = MainConfig.name


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
]
