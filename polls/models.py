from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
    """
    Question Model.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)
    total_votes = models.IntegerField(default=0) 

    def __str__(self):
        return self.question_text

    def save(self):
        """
        On save, will update the total votes.
        """
        self.total_votes = self.get_total_votes()
        return super(Question, self).save()

    def was_published_recently(self):
        """
        Check if question was published recently.
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def get_total_votes(self):
        """
        Returns the total adition of the results of instance question.
        """
        total_votes = 0
        for choice in self.choice_set.all():
            total_votes += choice.votes

        return total_votes
        

@python_2_unicode_compatible
class Choice(models.Model):
    """
    This model will represent the choices of every Question. All choices
    must have a relation with a Question instance.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text