# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Counter(models.Model):
	title = models.CharField(max_length=20)
	count = models.IntegerField()

	def __str__(self):
		return 'Title: {} and Count: {}'.format(self.title, self.count)