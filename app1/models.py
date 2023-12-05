from django.db import models
from datetime import date
class showManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['tname'])<2:
            errors['tname']="Title should be at least tow char"
        if len(postData['net'])<3:
            errors['net']="Network should be at least three char"
        if len(postData['desc'])<10:
            errors['desc']="Description  should be at least 10 char"
        if len(postData['releasedate'])==0:
            errors['releasedate']="Date should be added"
        if len( Show.objects.filter(title= postData['tname']))>0:
            errors['tname']="title should be uniqe"

        return errors
    
    def basic_validator2(self,postData):
        errors1={}
        if len(postData['ttname'])<2:
            errors1['ttname']="Title should be at least tow char"
        if len(postData['nett'])<3:
            errors1['nett']="Network should be at least three char"
        if len(postData['descr'])<10:
            errors1['descr']="Description  should be at least 10 char"

        if len(postData['releasedatee'])==0:
            errors1['releasedatee']="Date should be added"
        return errors1

class Show (models.Model):
    title=models.CharField(max_length=45)
    network=models.CharField(max_length=45)
    releasedate =  models.DateField(("Date"), default=date.today)
    description=models.TextField()
    creates_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=showManager()

    def creatshow(network1,title1,description1,reldate):
        print("hiii")
        print(reldate)
        return Show.objects.create(title=title1,network=network1,description=description1,releasedate =reldate)
    def readshow():
        return Show.objects.all()
    def readone():
       return Show.objects.last()
    
# Create your models here.
