# from django.http import Http404 # No longer needed with `get_object_or_404` shortcut
from django.shortcuts import get_object_or_404, render

"""
The following imports are no longer if using the `render()` shortcut (imported above) to render templates for all `views`
"""
from django.http import HttpResponse
# from django.template import loader

from .models import Question

# Display this at `localhost:8000/polls/`
def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  
  # * Display latest 5 poll questions separated by comma
  # output = ", ".join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)

  # * Load `index` template instead of previous hard-coded response
  # template = loader.get_template("polls/index.html")
  # context = {
  #   "latest_question_list": latest_question_list,
  # }
  # return HttpResponse(template.render(context, request))
  
  # * Using `render()` shortcut:
  context = {"latest_question_list": latest_question_list}
  return render(request, "polls/index.html", context)

def detail(request, question_id):
  # * Basic stub response
  # return HttpResponse("You're looking at question %s." % question_id)

  # * Attempt to load `detail` template or raise 404
  # try:
  #   question = Question.objects.get(pk=question_id)
  # except Question.DoesNotExist:
  #   raise Http404("Question does not exist")
  # return render(request, "polls/detail.html", {"question": question})

  # * Using `get_object_or_404()` shortcut
  question = get_object_or_404(Question, pk=question_id)
  return render(request, "polls/detail.html", {"question": question})

def results (request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

def vote(request, question_id):
  return HttpResponse("You're voting on question %s." % question_id)
