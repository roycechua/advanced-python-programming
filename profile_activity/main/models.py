from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    exp_years = models.IntegerField()
    college_degree = models.CharField(max_length=200)
    contact = models.CharField(max_length=15)
    email_address = models.EmailField()
    cv = models.FileField(blank=True,upload_to="cv")
    profile_pic = models.ImageField(blank=True,upload_to='profile_pics')
    about_me = models.TextField()

    def __str__(self):
        return self.full_name

class JobPosition(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    job_description = models.TextField()
    year_from = models.DateField()
    year_to = models.DateField()

    def __str__(self):
        return self.job_title