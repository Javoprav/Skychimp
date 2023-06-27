from random import sample

import django
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from blog.models import Post
from main.models import *
from main.services import send_email
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'main/index.html'
    extra_context = {
        'title': 'Главная страница',
        'object_list': Sending.objects.all()
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_posts = list(Post.objects.all())
        context['random_blog_posts'] = sample(all_posts, min(3, len(all_posts)))
        return context


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    extra_context = {
        'object_list': Customer.objects.all(),
        'title': 'Все клиенты'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('main.view_client'):
            return queryset
        return Customer.objects.filter(created_by=self.request.user)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    fields = ('name', 'email', 'comment', 'created_by')
    success_url = reverse_lazy('main:customer_list')


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    fields = ('name', 'email', 'comment', 'created_by', 'is_active')

    def get_success_url(self):
        return reverse('main:customer_view', args=[str(self.object.pk)])


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    success_url = reverse_lazy('main:customer_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'message_list': Message.objects.all(),
        'title': 'Все Сообщения'
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

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('main.view_sending'):
            return queryset
        return Sending.objects.filter(created=self.request.user)


class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending


class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    fields = ('message', 'frequency', 'status', 'created', 'scheduled_time', 'start_date', 'end_date', )
    success_url = reverse_lazy('main:sending_list')
    try:
        for send in Sending.objects.all():
            if send.status == Sending.CREATED:
                send_email(Sending.ONCE)
    except django.db.utils.ProgrammingError:
        print('ProgrammingError')


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
        'title': 'Все Рассылки'
    }


class AttemptDetailView(LoginRequiredMixin, DetailView):
    model = Attempt


def set_is_active(request, pk):
    customer_item = get_object_or_404(Customer, pk=pk)
    if customer_item.is_active:
        customer_item.is_active = False
    else:
        customer_item.is_active = True
    customer_item.save()
    return redirect(reverse('main:customer_list'))


def set_status_sending(request, pk):
    sending_item = get_object_or_404(Sending, pk=pk)
    if sending_item.status == Sending.CREATED:
        sending_item.status = Sending.COMPLETED
        sending_item.save()
    else:
        sending_item.status = Sending.CREATED
        sending_item.save()
    return redirect(reverse('main:sending_list'))
