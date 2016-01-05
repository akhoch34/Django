from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django import forms
# Create your models here.


@python_2_unicode_compatible
class Options(models.Model):
    n_size_choices = (('Unigram', '1'),
                      ('Bigram', '2'),
                      ('Trigram', '3'),
                      )
    n_size = models.CharField(max_length=1, choices=n_size_choices, default=n_size_choices[0])
    input_text = models.TextField()
    summary_text = models.TextField()

    def __str__(self):
        return self.input_text


