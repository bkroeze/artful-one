from django.urls import path
from . import views

app_name = "filedrop"

urlpatterns = [
    path("<slug:shortname>/", views.FileDownloadView.as_view(), name="download"),
]
