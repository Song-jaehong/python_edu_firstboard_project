from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from gallaryapp.models import Gallary
from gallaryapp.forms import GallaryCreationForm
from django.urls import reverse_lazy


class GallaryCreateView(CreateView):
    model = Gallary
    form_class = GallaryCreationForm
    template_name = "gallaryapp/create.html"
    success_url = reverse_lazy('gallaryapp:list')


class GallaryListView(ListView):
    model = Gallary
    context_object_name = "gallary_list"
    template_name = "gallaryapp/list.html"
    paginate_by = 30


class GallaryDetailView(DetailView):
    model = Gallary
    context_object_name = "target_gallary"
    template_name = "gallaryapp/detail.html"


class GallaryUpdateView(UpdateView):
    model = Gallary
    context_object_name = "target_gallary"
    form_class = GallaryCreationForm
    template_name = "gallaryapp/update.html"
    success_url = reverse_lazy('gallaryapp:list')


class GallaryDeleteView(DeleteView):
    model = Gallary
    context_object_name = "target_gallary"
    template_name = "gallaryapp/delete.html"
    success_url = reverse_lazy('gallaryapp:list')
