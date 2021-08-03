from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.CharField(max_length=300)
    vote_count = models.IntegerField(default=0)
    views = models.CharField(max_length=50)
    tags = models.CharField(max_length=250)

    def __str__(self):
        return self.question

