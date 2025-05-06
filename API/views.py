from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views import View

from .models import File
from .forms import FileForm

# Create your views here.


class UploadView(CreateView):
    model = File
    form_class = FileForm
    template_name = "upload.html"
    success_url = reverse_lazy("file_list")


class FileListView(ListView):
    model = File
    template_name = "file_list.html"
    context_object_name = "files"


class FileDetailView(DetailView):
    model = File
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("file_list")
