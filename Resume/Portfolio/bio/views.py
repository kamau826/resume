from django.shortcuts import render,redirect
from . models import About,Skills,Experience,Project,Messages
# from sms import send_sms
from django.core.mail import send_mail
from .forms import MessageForm
# Create your views here.
def index(request):
	about=About.objects.all()
	skills=Skills.objects.all()
	exp=Experience.objects.all()
	projects=Project.objects.all()
	if request.method=='POST':
		email=request.POST['email']
		text=request.POST['message']
		message=Messages(text=text,email=email)
		message.save()
		return redirect('index')
	context={
		'about':about,
		'skills':skills,
		'exp':exp,
		'projects':projects,
		
	}
	return render(request,'Portfolio/index.html',context)

def sendMail(request):
	send_mail(

		'hello from django',
		'kamau4542@gmail.com',
		['kjymooh@gmail.com'],
		fail_silently=False,

		)
def contact(request):
	form=MessageForm()
	


	context={
		'form':form
	}
	return render(request,'Portfolio/contactform.html',context)