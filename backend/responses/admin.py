from django.contrib import admin
from django.contrib.admin.widgets import AdminTextInputWidget
from django.db import models

from responses.models import Answer, Response


# Register your models here.
class Admin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminTextInputWidget},
    }


@admin.register(Answer)
class AnswerAdmin(Admin):
    pass


@admin.register(Response)
class ResponseAdmin(Admin):
    pass
