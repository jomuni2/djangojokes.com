from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from .models import Joke

# Register your models here.
@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('created', 'updated')
        
        return()