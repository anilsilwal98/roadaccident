from django.db import models

class  District(models.Model):
    name = models.CharField(max_length=200)

    def  __unicode__(self):
        return self.name

class  Location(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District)
 
    def  __unicode__(self):
        return self.name 

class  Case(models.Model):
    streetname = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    cause = models.CharField(max_length=200)
    location = models.ForeignKey(Location)
    
    def  __unicode__(self):
        return self.streetname

class  Victim(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    vehicletype = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    injury = models.CharField(max_length=100)
    case = models.ForeignKey(Case)
    
    def  __unicode__(self):
        return self.age

class  Mistakemaker(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    vehicletype = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    injury = models.CharField(max_length=100)
    case = models.ForeignKey(Case)

    def  __unicode__(self):
        return self.age


# Create your models here.
