from django.contrib import admin

# Import your models here.
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

