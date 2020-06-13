from django.db import models

# Create your models here.
class Pofol(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
