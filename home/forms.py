from django import forms
from home.models import Post

class HomeForm(forms.ModelForm):
	recruiter = forms.CharField()
	date = forms

	class Meta: 
		model = interview
		fields = ('recruiter','date','start_time','end_time','room_number')
