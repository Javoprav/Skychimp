from django.contrib import admin
from django.urls import path, include
from main.apps import MainConfig
from main.views import *

app_name = MainConfig.name


urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('sending/', SendingListView.as_view(), name='sending_list'),
    path('sending/<int:pk>/', SendingDetailView.as_view(), name='sending_view'),
    path('sending/create/', SendingCreateView.as_view(), name='sending_create'),
    path('sending/update/<int:pk>/', SendingUpdateView.as_view(), name='sending_update'),
    path('sending/delete/<int:pk>/', SendingDeleteView.as_view(), name='sending_delete'),
    path('attempt/', AttemptListView.as_view(), name='attempt_list'),
    path('attempt/<int:pk>/', AttemptDetailView.as_view(), name='attempt_view'),
]
