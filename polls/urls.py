from django.urls import path

from . import views

"""
Django uses `urlpatterns` variable to interpret URLs
Params from URLs are interpreted using angle brackets
  This object contains a data type converter, colon separator, and param name.
    Path converters : https://docs.djangoproject.com/en/5.1/topics/http/urls/#path-converters
"""

# Add "polls" namespace
app_name = "polls"
# Set routes for `./views.py`
urlpatterns = [
  # Route: /polls/
  path("", views.IndexView.as_view(), name="index"),
  # Route: /polls/:id/
  path("<int:pk>/", views.DetailView.as_view(), name="detail"),
  # Route: /polls/:id/results
  path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
  # Route: /polls/:id/vote/
  path("<int:question_id>/vote/", views.vote, name="vote"),
]
