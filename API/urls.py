from django.urls import path
from .views import UploadView, FileListView, FileDetailView, MarkdownCheckView, ShowView

urlpatterns = [
    path("upload/", UploadView.as_view(), name="upload"),
    path("files/", FileListView.as_view(), name="file_list"),
    path("files/delete/<int:pk>/", FileDetailView.as_view(), name="delete"),
    path('check/', MarkdownCheckView.as_view(), name="check"),
    path('show/', ShowView.as_view(), name="show_text"),
]
