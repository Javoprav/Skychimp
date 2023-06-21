from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.conf import settings
from django.http import Http404
from main.models import Customer, Sending, Attempt, Message
from main.services import send_email
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Sending.objects.all()
    }


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    # permission_required = 'main.view_customer'
    extra_context = {
        'object_list': Customer.objects.all(),
        'title': 'Все клиенты'  # дополнение к статической информации
    }

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     queryset = queryset.filter(created_by=user)
    #     return queryset

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if self.object.user != self.request.user:
    #         raise Http404("Вы не являетесь владельцем этого товара")
    #     return self.object


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
        'title': 'Все Рассылки'
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
