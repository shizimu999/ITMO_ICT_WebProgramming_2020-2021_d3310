from django.db import models
class person(models.Model):
        name = models.CharField(null=True, blank=True, max_length=15)
        age = models.CharField(null=True, blank=True, max_length=5)
        gender = models.CharField(null=True, blank=True, max_length=5)
        bir = models.DateTimeField(null=True, blank=True, max_length=15)
        class Meta:
             db_table = "person"

class address(models.Model):
        country = models.CharField(null=True, blank=True, max_length=200)
        province = models.CharField(null=True, blank=True, max_length=200)
        city = models.CharField(null=True, blank=True, max_length=200)
        street = models.CharField(null=True, blank=True, max_length=200)
        specific_information = models.CharField(null=True, blank=True, max_length=200)
        birthplace = models.CharField(null=True, blank=True, max_length=200)
        class Meta:
             db_table = "address"

class educational_background(models.Model):
        academic_degree = models.CharField(null=True, blank=True, max_length=200)
        paper = models.CharField(null=True, blank=True, max_length=200)
        achievement = models.CharField(null=True, blank=True, max_length=200)
        tutor = models.CharField(null=True, blank=True, max_length=200)
        University = models.CharField(null=True, blank=True, max_length=200)
        class Meta:
             db_table = "educational backgroun"

class interpersonal_relationship(models.Model):
        family_members = models.CharField(null=True, blank=True, max_length=200)
        friends = models.CharField(null=True, blank=True, max_length=200)
        colleague = models.CharField(null=True, blank=True, max_length=200)
        class Meta:
              db_table = "interpersonal relationship"
