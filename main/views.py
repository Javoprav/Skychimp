from django.shortcuts import render
from django.views.generic import ListView, DetailView
from main.models import Customer


class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer