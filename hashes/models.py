from django.db import models

class Hashes(models.Model):
    """Model to save our hash information"""
    title   = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    #automatically add timestamps when object is created 
    added_at = models.DateTimeField(auto_now_add=True) 
    #automatically add timestamps when object is updated
    last_update = models.DateTimeField(auto_now=True) #

class Tweets(models.Model):
    added_at = models.DateTimeField(auto_now_add=True) 
    last_update = models.DateTimeField(auto_now=True)   
    tweet_timestamp = models.CharField(max_length=255)
    tweet_id  =   models.IntegerField()
    tweet_user_id = models.CharField(max_length=255)
    content = models.CharField(max_length=140)
    positiveness = models.FloatField()
