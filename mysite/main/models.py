from django.db import models

# Create your models here.
class Training(models.Model):
    training_title = models.CharField(max_length=200)
    training_content = models.TextField()
    training_schedule = models.DateTimeField("Training Schedule")

    def __str__(self):
        return self.training_title