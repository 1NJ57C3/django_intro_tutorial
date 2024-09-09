from django.shortcuts import render

from django.http import HttpResponse

# Display this at `localhost:8000/polls/`
def index(request):
  return HttpResponse("Goodbye, world. You're at the polls index.")
