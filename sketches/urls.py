from django.urls import path
from . import views

urlpatterns = [
    path("", views.sketch_landing, name="sketch_landing"),
    path("<slug:slug>/", views.sketch_detail, name="sketch_detail"),
]
