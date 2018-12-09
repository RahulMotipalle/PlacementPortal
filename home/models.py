# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model):	
	student_name=models.CharField(max_length=100)	
	student_id=models.CharField(default="",null=False,max_length=50)
	cgpa=models.FloatField()
	gender=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)
	#birthdate=models.DateField()
	present_addess=models.CharField(max_length=100)
	email_id=models.CharField(max_length=100)
	projects=models.TextField(default="Simple Website",null=False)	
	internships=models.TextField(default="TCS, Google",null=False)
	achievements=models.TextField(default="EG: Awarded the title of 'Best Public Speaker' in college",null=False)
	
	def __str__(self):
		return str(self.student_name)

	
class Recruiter(models.Model):
	recruiter_name=models.CharField(max_length=100, default="Company1")
	password=models.CharField(max_length=100, default='12345678')	
	sector=models.CharField(max_length=20)
	branch=models.CharField(max_length=20)
	address=models.CharField(max_length=100)
	website=models.CharField(max_length=100)
	email_id=models.CharField(max_length=100)
	max_salary=models.IntegerField(default=700000)

	def __str__(self):
		return str(self.recruiter_name)


class Record(models.Model):
	student=models.ForeignKey(Student,on_delete=models.SET_NULL,null=True)
	recruiter=models.ForeignKey(Recruiter,on_delete=models.SET_NULL,null=True)
	passout_year=models.CharField(max_length=10)
	salary=models.IntegerField()

	def __str__(self):
		return "Student ID " + str(self.student_id) + " hired by Company ID " + str(self.recruiter_id) 		

class Coordinator(models.Model):
	coordinator=models.CharField(max_length=50)
	coordinator_name=models.CharField(max_length=100)
	password=models.CharField(max_length=100, default='12345678')	
	programme=models.CharField(max_length=10)
	department=models.CharField(max_length=10)
	contact_number=models.CharField(max_length=20)
	email_id=models.CharField(max_length=100)
	
	def __str__(self):
		return str(self.coordinator_name)


class Hiringtest(models.Model):
	recruiter_name=models.CharField(max_length=50, default="company1", editable=True, null=False)
	test_type=models.CharField(max_length=200,null=False)
	round_number=models.IntegerField(default=1,null=False)
	test_date=models.CharField(max_length=20, default="02/11/2018", editable=True, null=False)
	gpa_cutoff=models.CharField(max_length=10,null=False)

	def __str__(self):
		return str(self.recruiter_name) + "'s hiring test: Round No. " + str(self.round_number)
		

class Interview(models.Model):
	recruiter_name=models.CharField(max_length=50, default="company1", editable=True, null=False)
	#date=models.DateField(null=True) 
	date=models.CharField(max_length=20, default="02/11/2018", editable=True, null=False)
	start_time=models.CharField(max_length=10,default="10 am", editable=True, null=False)
	end_time=models.CharField(max_length=10,default="10 am", editable=True, null=False)
	room_type=models.CharField(max_length=50)
	
	def __str__(self):
		return str(self.recruiter_name) + "'s interview"


class Vacancy(models.Model):
	recruiter_name=models.CharField(max_length=50, default="EG: Company1", null=False)
	designation=models.CharField(max_length=200, default="EG: Jr. Software Developer/Summer Intern etc.", null=False)	
	technical_skills=models.CharField(max_length=200, default="EG: Python", null=False)
	other_skills=models.CharField(max_length=200, default="EG: Good communication skills etc.", null=False)
	expected_salary=models.CharField(max_length=20, null=False, default="EG: 700000")

	def __str__(self):
		return str(self.designation) + " at " + str(self.recruiter_name)


class Testimonial(models.Model):
	employee_name=models.CharField(max_length=60, default="EG: John Doe", null=False)
	recruiter_name=models.CharField(max_length=50, default="EG: Company1", null=False)
	remarks=models.TextField(null=False)
	
	def __str__(self):
		return str(self.employee_name) + " from " + str(self.recruiter_name) + " says: "
