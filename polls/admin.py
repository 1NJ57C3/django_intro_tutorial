from django.contrib import admin

# Import Question model
from .models import Question

# Add Question model to Admin panel
admin.site.register(Question)
