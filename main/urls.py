from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.decorators.cache import never_cache

from main.apps import MainConfig
from main.views import *

app_name = MainConfig.name


urlpatterns = [
    path('', never_cache(IndexView.as_view()), name='Index'),
    path('customer/', never_cache(CustomerListView.as_view()), name='customer_list'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_view'),
    path('customer/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customer/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('message/', never_cache(MessageListView.as_view()), name='message_list'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message_view'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('sending/', never_cache(SendingListView.as_view()), name='sending_list'),
    path('sending/<int:pk>/', SendingDetailView.as_view(), name='sending_view'),
    path('sending/create/', SendingCreateView.as_view(), name='sending_create'),
    path('sending/update/<int:pk>/', SendingUpdateView.as_view(), name='sending_update'),
    path('sending/delete/<int:pk>/', SendingDeleteView.as_view(), name='sending_delete'),
    path('attempt/', never_cache(AttemptListView.as_view()), name='attempt_list'),
    path('attempt/<int:pk>/', AttemptDetailView.as_view(), name='attempt_view'),
    path('set_is_active/<int:pk>', login_required(set_is_active), name='set_is_active'),
    path('set_status_sending/<int:pk>', login_required(set_status_sending), name='set_status_sending')
]
