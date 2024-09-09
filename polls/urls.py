from django.urls import path

from . import views

# Set route for `./views.py`
urlpatterns = [
  path("", views.index, name="index"),
]
