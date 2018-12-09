# -*- coding: utf-8 -*-s
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.views.generic import TemplateView, RedirectView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import *
import string 
import random 
import requests


global_name=None
global_studentid=None
global_ug=None
global_emailid=None
global_mobileno=None


def landing(request):
	return render(request, 'landing.html')


def main(request, token_id):	
	global global_studentid
	global global_name
	global global_emailid
	global global_mobileno
	global global_ug
	global global_studentdob
	
	print("This is token ID {}".format(token_id))
	payload={'token':token_id, 	'secret':"0c5df65d098163dca4e1087398795788d94c13d6a3cf6f6e9594d15af850df3bd1997fe9ddd4e6f40efcd469548bca10eb18fd7226fb9798a613161da9f30bee"}
	url="https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"	
	response=requests.post(url,data=payload)
	data=response.json()

	print("Details from API:",data)
	print("************************",data['student'][0]['Student_ID'])	
	global_studentid=data['student'][0]['Student_ID']
	global_name=data['student'][0]['Student_First_Name']
	global_emailid=data['student'][0]['Student_Email']
	global_mobileno=data['student'][0]['Student_Mobile']
	global_ug=data['student'][0]['Student_Cur_YearofStudy']
	global_studentdob=data['student'][0]['Student_DOB']	
	
	print("\n\n\n\n")
	#gp=Student.objects.all().filter(student_name__exact=global_name)
	

	data=data['student']
	#print("data2",data.student)	
	recs=Record.objects.all().order_by('-salary')
	context={"Records": recs, "uid": global_studentid, "global_name": global_name}
	return render(request,'main.html', context)


#-------------------------------------------------------------------FOR RECRUITER USECASES---------------------------------------------------------#


def index(request):
	return render(request, 'index.html', {"Students":Student.objects.all(), "Testimonials":Testimonial.objects.all()})


#@login_required(login_url='/recruiterlogin/')
def viewprofiles(request):	
	studs=Student.objects.all().order_by('-cgpa')			#retrieving student details in descending order of CGPAs (from highest to least)	
	context={'Students': studs}	
	return render(request, 'viewprofiles.html', context)

def eceprofiles(request):
	studs=Student.objects.all().order_by('-cgpa')		
	ecestuds=studs.filter(branch='ECE')						#filtering student table to get only ECE students' details
	context={'Students': ecestuds}			
	return render(request, 'eceprofiles.html', context)	

def cseprofiles(request):
	studs=Student.objects.all().order_by('-cgpa')
	csestuds=studs.filter(branch='CSE')						#filtering student table to get only CSE students' details
	context={'Students': csestuds}
	return render(request, 'cseprofiles.html', context)

def descending(request):
	studs=Student.objects.all().order_by('-cgpa')			#retrieving student details in descending order of CGPAs 
	context={'Students': studs}	
	return render(request, 'viewprofiles.html', context)

def ascending(request):
	studs=Student.objects.all().order_by('cgpa')			#retrieving student details in ascending order of CGPAs 	
	context={'Students': studs}	
	return render(request, 'viewprofiles.html', context)


def displaylogin(request):
	return render(request, 'login.html')

def recruiterlogin(request):
	if request.method== 'POST':
		if request.POST.get('username', False) != False and request.POST.get('password', False) != False:
			p=request.POST.get('username', False)
			q=request.POST.get('password', False)
			if (Recruiter.objects.filter(recruiter_name= p, password=q).exists() == True):
				return render(request,'index.html', { 'name': request.POST.get('username', False) })
			else:
				return render(request,'login.html')

def displayclogin(request):
	return render(request, 'clogin.html')

def coordinatorlogin(request):
	if request.method== 'POST':
		if request.POST.get('username', False)!= False and request.POST.get('password', False) != False:
			p=request.POST.get('username', False)
			q=request.POST.get('password', False)
			if (Coordinator.objects.filter(coordinator_name= p, password=q).exists()):
				return render(request,'placementhome.html')
			else:
				return render(request,'clogin.html')


def stat(request):
	return render(request, 'stat.html')


def scheduleinterview(request):
	if request.method=='POST':
		inter=Interview()										#Accessing Interviews table
		inter.recruiter_name=request.POST['recruiter_name']		#Fetching all details of interview
		inter.date=request.POST['date']
		inter.start_time=request.POST['start_time']
		inter.end_time=request.POST['end_time']
		inter.room_type=request.POST['room_type']
		inter.save()											#Storing the entered details to database
		#return render(request, 'index.html')
	interviews=Interview.objects.all()
	#context={"interviews": interviews}
	context={"interviews": interviews, "name": request.GET.get('name')}
	return render(request, 'scheduleinterview.html',context)

#def search(request):        

def conducthiringtest(request):
	if request.method=='POST':
		htest=Hiringtest()
		htest.recruiter_name=request.POST['recruiter_name']
		htest.test_type=request.POST['test_type']
		htest.round_number=request.POST['round_number']
		htest.test_date=request.POST['test_date']
		htest.gpa_cutoff=request.POST['gpa_cutoff']
		htest.save()
	hiringtests=Hiringtest.objects.all()
	context={"hiringtests": hiringtests, "name": request.GET.get('recruiter_name')}
	return render(request, 'hiringtest.html', context)




#Storing the vacancies added by the recruiter to the database
def addvacancies(request):
	if request.method=='POST':
		vac=Vacancy()
		vac.recruiter_name=request.POST['recruiter_name']
		vac.designation=request.POST['designation']
		vac.technical_skills=request.POST['technical_skills']
		vac.other_skills=request.POST['other_skills']
		vac.expected_salary=request.POST['expected_salary']
		vac.save()
	vacancies=Vacancy.objects.all()
	context={"vacancies":vacancies, "name": request.GET.get('name')}
	return render(request,'vacancies.html', context)


def viewnoticeboard(request):
	return render(request, 'noticeboard2.html', {"Recruiters":Recruiter.objects.all(), "Interviews":Interview.objects.all(), "Hiringtests": Hiringtest.objects.all(), "Vacancys": Vacancy.objects.all().order_by('-expected_salary')})



#Storing the entered testimonials in the testimonial page to the database
def writetestimonials(request):
	if request.method=='POST':
		testimony=Testimonial()
		testimony.employee_name=request.POST['employee_name']
		testimony.recruiter_name=request.POST['recruiter_name']
		testimony.remarks=request.POST['remarks']
		testimony.save()
	testimonials=Testimonial.objects.all()
	context={"testimonials":testimonials, "name": request.GET.get('name')}	
	return render(request,'testimonials.html', context)



def page(request):
	return render(request, 'index.html', {"Students":Student.objects.all(), "Testimonials":Testimonial.objects.all()})

def visitcampus(request):
	return render(request,'visitcampus.html')



#-----------------------------------------------------FOR STUDENT USECASES---------------------------------------------------------------#

def studenthome(request):
	global global_studentid	
	global global_name	
	gp=Student.objects.all().filter(student_name__exact=global_name)
	print(gp)
		
	recs=Record.objects.all().order_by('-salary')
	context={"Records": recs, "uid": global_studentid, "global_name": global_name}
	return render(request,'studenthome.html', context)	

def studentnoticeboard(request):
	return render(request, 'noticeboard.html', {"Recruiters":Recruiter.objects.all(), "Interviews":Interview.objects.all(), "Hiringtests": Hiringtest.objects.all(), "Vacancys": Vacancy.objects.all().order_by('-expected_salary')})

def apply(request):
	return render(request, 'apply.html')



#For viewing all the companies visiting this year
def browse(request):
	recs=Recruiter.objects.all().order_by('-max_salary')
	context={"Recruiters": recs}
	return render(request,'browse.html', context)

def itcompanies(request):
	comps=Recruiter.objects.all().filter(max_salary=700000)
	context={"Companies": comps}
	return render(request, 'itcompanies.html', context)


#def cseprofiles(request):
#	studs=Student.objects.all().order_by('-cgpa')
#	csestuds=studs.filter(branch='CSE')						#filtering student table to get only CSE students' details
#	context={'Students': csestuds}
#	return render(request, 'cseprofiles.html', context)


def corecompanies(request):
	coms=Recruiter.objects.all().order_by('-max_salary')
	corecomps=coms.filter(sector="Core")
	context={"Companies": corecomps}
	return render(request, 'corecompanies.html', context)		




def details(request):
	return render(request, 'details.html')

#def pastrecruiters(request):
#	return render(request, 'pastrecruiters.html')

#def viewprofile(request):
	#return render(request, 'viewprofile.html')


#Saving the details entered by the student to the database
def upload(request):
	global global_studentid 
	global global_name
	global global_emailid
	global global_mobileno
	global global_ug
	
	if request.method=='POST':
		stud=Student()
		stud.student_id=global_studentid		
		stud.student_name=global_name
		stud.cgpa=request.POST['cgpa']
		stud.email_id=global_emailid
		stud.present_address=request.POST['present_address']
		stud.branch=request.POST['branch']
		stud.projects=request.POST['projects']
		stud.internships=request.POST['internships']
		stud.achievements=request.POST['achievements']
		stud.save()
	students=Student.objects.all()	
	context={"students": students, "stud_id": global_studentid, "stud_name": global_name, "stud_email": global_emailid, "phone_no": global_mobileno, "yearofstudy": global_ug}		
	return render(request, 'upload.html', context)



def studentstats(request):
	return render(request, 'studentstats.html')


#FOR PLACEMENT COORDINATOR USECASES:

def placementhome(request):
	return render(request, 'placementhome.html')

def enlist(request):
	studs=Student.objects.all().order_by('-cgpa')			#retrieving student details in descending order of CGPAs (from highest to least)	
	context={'Students': studs}	
	return render(request, 'enlist.html', context)

def addrecord(request):
	if request.method=='POST':
		reco=Record()
		reco.student_id=request.POST['student_id']
		reco.recruiter_id=request.POST['recruiter_id']
		reco.passout_year=request.POST['passout_year']
		reco.salary=request.POST['salary']
		reco.save()
	records=Record.objects.all()
	context={"Records": records}
	return render(request, 'record.html', context)

def viewplacementrecord(request):
	recs=Record.objects.all().order_by('-salary')
	context={"Records": recs}
	return render(request, 'viewplacementrecord.html', context)		

def deletestudent(request):
	return render(request, 'http://localhost:8002/admin/home/student/', context)
