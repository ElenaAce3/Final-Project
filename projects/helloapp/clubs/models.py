from django.db import models

# Create your models here.
class School(models.Model):
    school_name = models.CharField(max_length=30)
    school_code = models.CharField(max_length=6)
    #id is written for us
    pass #the CLUB POINTS TO THE School

#many to one relationship
class Club(models.Model):
    club_name = models.CharField(max_length=30)
    club_bio = models.CharField(max_length=250)
    club_contact = models.CharField(max_length=250)
    club_meeting = models.CharField(max_length=250)
    club_event = models.CharField(max_length=250)
    #add in image later
    #club_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    club_school = models.ForeignKey(School, on_delete=models.CASCADE)
    #id written for us
