from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import File
from .forms import FileForm

# Create your views here.

class UploadView(CreateView):
    model = File
    form_class = FileForm
    success_url = reverse_lazy('file_list')


class FileListView(ListView):
    model = File
    context_object_name = 'file'


