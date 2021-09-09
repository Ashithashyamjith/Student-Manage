from django.db import models


# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=25)
    

class Registration(models.Model):
    user_id=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    contact=models.IntegerField()
    email=models.EmailField(max_length=25)

class Studentstatus(models.Model):
    user_log=models.ForeignKey(Login,on_delete=models.CASCADE)
    stud=models.ForeignKey(Registration,on_delete=models.CASCADE)
    status=models.CharField(max_length=25)

