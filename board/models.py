# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import uuid

# Create your models here.

class Author(models.Model):
    name    =   models.CharField(max_length=256)
    key     =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Topic(models.Model):
    title   =   models.CharField(max_length=256)
    desc    =   models.TextField()
    author  =   models.ForeignKey(Author)
    created =   models.DateTimeField(auto_now_add=True)
    key     =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Comment(models.Model):
    text    =   models.TextField()
    author  =   models.ForeignKey(Author)
    thread  =   models.ForeignKey(Topic)
    created =   models.DateTimeField(auto_now_add=True)
    key     =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
