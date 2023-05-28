from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Customer


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