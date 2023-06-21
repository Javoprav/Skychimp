from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from main.models import Customer, Sending, Attempt, Message
from main.services import send_email
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class CustomerListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Customer
    permission_required = 'main.view_customer'
    extra_context = {
        'object_list': Customer.objects.all(),
        'title': 'Все клиенты'  # дополнение к статической информации
    }


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ('name', 'email', 'message',)
    success_url = reverse_lazy('main:customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ('name', 'email', 'message',)

    def get_success_url(self):
        return reverse('main:customer_view', args=[str(self.object.pk)])


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('main:customer_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'message_list': Message.objects.all(),
        'title': 'Все Сообщения'  # дополнение к статической информации
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ('subject', 'body', )
    success_url = reverse_lazy('main:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ('subject', 'body', )

    def get_success_url(self):
        return reverse('main:message_view', args=[str(self.object.pk)])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class SendingListView(LoginRequiredMixin, ListView):
    model = Sending
    extra_context = {
        'object_list': Sending.objects.all(),
        'title': 'Все Рассылки'  # дополнение к статической информации
    }


class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending


class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    fields = ('message', 'frequency', 'status', )
    success_url = reverse_lazy('main:sending_list')
    send_email(Sending.ONCE)


class SendingUpdateView(LoginRequiredMixin, UpdateView):
    model = Sending
    fields = ('message', 'frequency', 'status', )

    def get_success_url(self):
        return reverse('main:sending_view', args=[str(self.object.pk)])


class SendingDeleteView(LoginRequiredMixin, DeleteView):
    model = Sending
    success_url = reverse_lazy('main:sending_list')


class AttemptListView(LoginRequiredMixin, ListView):
    model = Attempt
    extra_context = {
        'object_list': Attempt.objects.all(),
        'title': 'Все Рассылки'  # дополнение к статической информации
    }


class AttemptDetailView(LoginRequiredMixin, DetailView):
    model = Attempt
