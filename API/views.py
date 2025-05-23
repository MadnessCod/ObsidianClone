from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView, TemplateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import File
from .forms import FileForm, TextFrom, OnlineForm


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


class FileDeleteView(DeleteView):
    model = File
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("file_list")


class MarkdownCheckView(FormView):
    form_class = TextFrom
    template_name = 'check.html'
    success_url = reverse_lazy("show_text")

    def form_valid(self, form):
        self.request.session['submitted_text'] = form.cleaned_data['text']
        return super().form_valid(form)


class ShowView(TemplateView):
    template_name = "show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = self.request.session['submitted_text']
        context['corrected'] = 'this is corrected text'
        return context


class FileDetailView(DetailView):
    model = File
    template_name = 'file_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        file_obj = self.object

        try:
            with file_obj.file.open('r') as f:
                content = f.read()
        except FileNotFoundError as e:
            content = f'[Error reading file: {e}'

        context['file_content'] = content
        return context
