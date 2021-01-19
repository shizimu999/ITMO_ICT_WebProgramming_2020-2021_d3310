from django.db import models

class Match(models.Model):
    locatoin=models.CharField(max_length=50)
    time=models.DateTimeField()

class comments(models.Model):
    comment=models.CharField(max_length=100)
    data=models.DateTimeField()
    commentator=models.CharField(max_length=50)
    ID_Match=models.ForeignKey(Match,null=True,blank=True,on_delete=models.SET_NULL)

class round(models.Model):
    Number_round=models.CharField(max_length=20)
    ID_Match = models.ForeignKey(Match, null=True, blank=True, on_delete=models.SET_NULL)

class group(models.Model):
    Group_name=models.CharField(max_length=50)
    ID_round=models.ForeignKey(round, null=True, blank=True, on_delete=models.SET_NULL)

class Racer(models.Model):
    racer_name=models.CharField(max_length=50)
    Introduction=models.CharField(max_length=100)
    rank=models.CharField(max_length=20)
    ID_group=models.ForeignKey(group, null=True, blank=True, on_delete=models.SET_NULL)

class Racing_car(models.Model):
    type_list=(('M','motorcycle'),('ort','Off road truck'),('SUV','offroad racing'))
    Vehicle_type=models.CharField(max_length=3,choices=type_list)
    ID_racer=models.ForeignKey(Racer, null=True, blank=True, on_delete=models.SET_NULL)

class result(models.Model):
    result=models.CharField(max_length=20)
    time_cost = models.CharField(max_length=20)
    ID_racer = models.ForeignKey(Racer, null=True, blank=True, on_delete=models.SET_NULL)
    ID_Match = models.ForeignKey(Match, null=True, blank=True, on_delete=models.SET_NULL)



