from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default = 1)
    image = models.ImageField(upload_to ='images/')
    body = models.TextField()
    supporter = models.TextField()
    numbersupp = models.IntegerField()
    hunter = models.TextField()


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def vote_up(self):
        self.votes_total + 1
