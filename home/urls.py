from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^main/(?P<token_id>[\w\.-]+)/',views.main,name="main"),
	#for recruiter usecases	
	url(r'^$',views.landing),
	url(r'^landing/$',views.landing,name='landing'),
	url(r'^displaylogin/$',views.displaylogin, name="displaylogin"),
	url(r'^displayclogin/$',views.displayclogin, name="displayclogin"),
	url(r'^recruiterlogin/$',views.recruiterlogin, name="recruiterlogin"),
	url(r'^coordinatorlogin/$',views.coordinatorlogin, name="coordinatorlogin"),
	url(r'^index/$',views.index, name="index"),
	
	#FOR VIEW PROFILES USECASE
	url(r'^viewprofiles/$',views.viewprofiles, name="viewprofiles"),
	url(r'^eceprofiles/$',views.eceprofiles, name='eceprofiles'),
	url(r'^cseprofiles/$',views.cseprofiles, name='cseprofiles'),
    url(r'^descending/$',views.descending, name='descending'),
    url(r'^ascending/$',views.ascending, name='ascending'),

	url(r'^scheduleinterview/$',views.scheduleinterview, name="scheduleinterview"),
	url(r'^hiringtest/$',views.conducthiringtest, name="conducthiringtest"),
	url(r'^noticeboard/$',views.viewnoticeboard, name="noticeboard"),	
	#url(r'^hirecandidates/$',views.hirecandidates, name="hirecandidates"),
	url(r'^testimonials/$',views.writetestimonials, name="writetestimonials"),
	url(r'^visitcampus/$',views.visitcampus, name="visitcampus"),
	url(r'^vacancies/$',views.addvacancies, name="addvacancies"),
	#url(r'^statistics/$',views.statistics, name="statistics"),
	

	#for student usecases
	url(r'^studenthome/$', views.studenthome, name="studenthome"),	
	url(r'^studentnoticeboard/$', views.studentnoticeboard, name="studentnoticeboard"),	
	url(r'^apply/$',views.apply,name="apply"),
	
	#FOR VIEW VISITING COMPANIES USECASE
	url(r'^browse/$',views.browse,name="browse"),
	url(r'^itcompanies/$',views.itcompanies,name="itcompanies"),
	url(r'^corecompanies/$',views.corecompanies,name="corecompanies"),	

	url(r'^details/$',views.details,name="details"),
	#url(r'^pastrecruiters/$',views.pastrecruiters,name="pastrecruiters"),
	url(r'^stat/$',views.stat,name="stat"),
	url(r'^viewprofile/$',views.stat,name="viewprofile"),
	url(r'^upload/$',views.upload,name="upload"),
	url(r'^studentstats/$',views.studentstats,name="studentstats"),

	#FOR PLACEMENT COORDINATOR USECASES
	url(r'^placementhome/$',views.placementhome,name="placementhome"),
	url(r'^viewplacementrecord/$',views.viewplacementrecord,name="viewplacementrecord"),	
	url(r'^enlist/$',views.enlist,name="enlist"),
	url(r'^record/$',views.addrecord,name="addrecord"),
	url(r'^deletestudent/$',views.deletestudent,name="deletestudent")
]  
