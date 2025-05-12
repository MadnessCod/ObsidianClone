from django.urls import path
from .views import (
    UploadView,
    FileListView,
    FileDeleteView,
    MarkdownCheckView,
    ShowView,
    FileDetailView
)

urlpatterns = [
    path("upload/", UploadView.as_view(), name="upload"),
    path("files/", FileListView.as_view(), name="file_list"),
    path("files/delete/<int:pk>/", FileDeleteView.as_view(), name="delete"),
    path("check/", MarkdownCheckView.as_view(), name="check"),
    path("show/", ShowView.as_view(), name="show_text"),
    path("files/detail/<int:pk>/", FileDetailView.as_view(), name="file_detail"),
]
