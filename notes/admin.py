# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ['title']

admin.site.register(Note, NoteAdmin)
