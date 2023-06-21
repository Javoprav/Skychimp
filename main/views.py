from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.conf import settings
from main.models import Customer, Sending, Attempt, Message
from main.services import send_email


class CustomerListView(ListView):
    model = Customer
    extra_context = {
        'object_list': Customer.objects.all(),
        'title': 'Все клиенты'  # дополнение к статической информации
    }


class CustomerDetailView(DetailView):
    model = Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = ('name', 'email', 'message',)
    success_url = reverse_lazy('main:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ('name', 'email', 'message',)

    def get_success_url(self):
        return reverse('main:customer_view', args=[str(self.object.pk)])


class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('main:customer_list')


class MessageListView(ListView):
    model = Message
    extra_context = {
        'message_list': Message.objects.all(),
        'title': 'Все Сообщения'  # дополнение к статической информации
    }


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ('subject', 'body', )
    success_url = reverse_lazy('main:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('subject', 'body', )

    def get_success_url(self):
        return reverse('main:message_view', args=[str(self.object.pk)])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('main:message_list')


class SendingListView(ListView):
    model = Sending
    extra_context = {
        'object_list': Sending.objects.all(),
        'title': 'Все Рассылки'  # дополнение к статической информации
    }


class SendingDetailView(DetailView):
    model = Sending


class SendingCreateView(CreateView):
    model = Sending
    fields = ('message', 'frequency', 'status', )
    success_url = reverse_lazy('main:sending_list')
    send_email(Sending.ONCE)


class SendingUpdateView(UpdateView):
    model = Sending
    fields = ('message', 'frequency', 'status', )

    def get_success_url(self):
        return reverse('main:sending_view', args=[str(self.object.pk)])


class SendingDeleteView(DeleteView):
    model = Sending
    success_url = reverse_lazy('main:sending_list')


class AttemptListView(ListView):
    model = Attempt
    extra_context = {
        'object_list': Attempt.objects.all(),
        'title': 'Все Рассылки'  # дополнение к статической информации
    }


class AttemptDetailView(DetailView):
    model = Attempt