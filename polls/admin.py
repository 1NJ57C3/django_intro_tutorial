from django.contrib import admin

# Import Question model
from .models import Choice, Question


# Part 7 - 
# class ChoiceInline(admin.StackedInline): # Stacks fields vertically
class ChoiceInline(admin.TabularInline): # Places fields horizontally inline, table-based
  model = Choice
  extra = 3


# Part 7 - Customize Admin Form
class QuestionAdmin(admin.ModelAdmin):
  # fields = ["pub_date", "question_text"] # * Move "pub_date" above "question_text" in editor
  fieldsets = [ # Split up form inputs into groups
    (None, {"fields": ["question_text"]}),
    ("Date information", {
      "fields": ["pub_date"], # fieldset object params: (title, fields)
      "classes": ["collapse"],
    }),
  ]
  # Add `Choice`s inputs to `Question` editor
  inlines = [ChoiceInline]
  # Add columns to list view
  list_display = ["question_text", "pub_date", "was_published_recently"]
  # Add filter widget to list view
  list_filter = ["pub_date"]
  # Add search widget to list view; uses SQL `LIKE` query
  search_fields = ["question_text"]
  # Adjust pagination / Questions per page; Default 100
  list_per_page = 20

# Add Question model to Admin panel
admin.site.register(Question, QuestionAdmin)
# Part 7 - Change site header without overriding entire admin template
admin.AdminSite.site_header = "Polls Administration"