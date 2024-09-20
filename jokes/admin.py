from typing import Any
from django.contrib import admin
from django.http import HttpRequest

from .models import Category, Joke

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')
        return ()

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    model = Joke
    list_display = ['question', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ('slug', 'created', 'updated')
        
        return()