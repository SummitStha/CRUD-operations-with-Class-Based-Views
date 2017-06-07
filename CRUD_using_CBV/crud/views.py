# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Counter
# Create your views here.

class CounterCreateView(CreateView):
	model = Counter
	template_name = 'create_counter.html'
	fields = '__all__'
	success_url = reverse_lazy('list-count')


class CounterUpdateView(UpdateView):
	model = Counter
	template_name = 'create_counter.html'
	fields = '__all__'
	success_url = reverse_lazy('list-count')
	# template_name_suffix = '_update_form'

class CounterDeleteView(DeleteView):
	model = Counter
	success_url = reverse_lazy('list-count')
	template_name = 'confirm_counter_delete.html'

class CounterDetailView(DetailView):
	model = Counter
	template_name = 'counter_detail.html'

	def get_context_data(self, **kwargs):
		context = super(CounterDetailView, self).get_context_data(**kwargs)
		return context


class CounterListView(ListView):
	model = Counter
	template_name = 'counter_list.html'

	def get_context_data(self, **kwargs):
		context = super(CounterListView, self).get_context_data(**kwargs)
		return context