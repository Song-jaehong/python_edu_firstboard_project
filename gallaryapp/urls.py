from django.urls import path
from gallaryapp.views import GallaryCreateView, GallaryListView, GallaryDetailView, GallaryUpdateView, GallaryDeleteView
app_name = "gallaryapp"

urlpatterns = [
    path("create/", GallaryCreateView.as_view(), name="create"),
    path("list/", GallaryListView.as_view(), name="list"),
    path("detail/<int:pk>", GallaryDetailView.as_view(), name="detail"),
    path("update/<int:pk>", GallaryUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", GallaryDeleteView.as_view(), name="delete"),
]
