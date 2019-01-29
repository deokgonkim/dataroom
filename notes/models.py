# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):

    guid = models.CharField(max_length=36)

    author = models.ForeignKey(User)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    title = models.TextField(blank=True)

    content = models.TextField(blank=True)

    def __unicode__(self):
        return self.title
