from django.db import models
from django.contrib.auth.models import User



class About(models.Model):
    img = models.ImageField(null=True , blank=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    skills = models.TextField() 
    # skills = models.ManyToManyField('Skill',blank=True )
    work_experience = models.ManyToManyField('Work', blank=True)
    education = models.ManyToManyField('Education', blank=True)
    

    email_id = models.EmailField(max_length=100, null=True , blank=True)
    website = models.CharField(max_length=100, null=True , blank=True)
    linkedin_url = models.CharField(max_length=100, null=True , blank=True)
    phone = models.CharField(max_length=13, null=True , blank=True)
    def __str__(self):
        return self.name 
    

class Work(models.Model):
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    desc = models.TextField(blank=True)  # use /n for new line seperator 
    skills = models.TextField(blank=True) 

    def __str__(self):
        return self.company_name

class Education(models.Model):
    school_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=100 , null=True , blank=True)

    def __str__(self):
        return self.school_name
