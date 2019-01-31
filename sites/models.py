# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

from datetime import datetime, timedelta

# Create your models here.

def yearafter():
    return datetime.now() + timedelta(days=30)

class WebSite(models.Model):

    guid = models.CharField(max_length=36)

    author = models.ForeignKey(User)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    title = models.TextField(blank=True)

    url = models.TextField(blank=True)

    favicon = models.TextField(blank=True)

    expiration = models.DateTimeField(default=yearafter)

    def __unicode__(self):
        return self.title
