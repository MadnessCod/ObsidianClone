from django.urls import path
from .views import UploadView, FileListView

urlpatterns = [
    path('upload/', UploadView.as_view(), name='upload'),
    path('file/', FileListView.as_view(), name='file_list'),
]
