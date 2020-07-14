import datetime

from django.db import models
from django.utils import timezone

class Representative(models.Model):
    rep_name = models.CharField(max_length=200)
    comittee = models.CharField(blank=True, max_length=200)
    website = models.URLField(blank=True,max_length=400)
    state = models.CharField(max_length=50)
    party = models.CharField(blank=True, max_length=20)
    def __str__(self):
        return self.rep_name
    def first_last_name(self):
        return self.rep_name.split(' ', 1)
class Senator(models.Model):
    sen_name = models.CharField(max_length=200)
    website = models.URLField(blank=True,max_length=400)
    state = models.CharField(max_length=50)
    party = models.CharField(blank=True, max_length=20)
    def __str__(self):
        return self.sen_name
    def first_last_name(self):
        return self.rep_name.split(' ', 1)

class Issue(models.Model):
    issue_name = models.CharField(max_length=200)
    issue_text = models.TextField()
    def __str__(self):
        return self.issue_name

class Vote(models.Model):
    vote_type = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    def __str__(self):
        if self.vote_type == 1:
            return ('Upvote')
        elif self.vote_type == 0:
            return ('Neutral')
        else:
            return ('Downvote')