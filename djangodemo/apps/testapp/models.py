from django.db import models


class Employee(models.Model):
	name = models.CharField(max_length=200)
	age = models.IntegerField(default=18)
	join_date = models.DateTimeField('joining date')

class Team(models.Model):
	employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
	team_name = models.CharField(max_length=200)
