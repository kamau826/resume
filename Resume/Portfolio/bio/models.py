from django.db import models

# Create your models here.
class Skills(models.Model):
	name=models.CharField(max_length=100)
	descr=models.TextField()

	def __str__(self):
		return self.name

class Experience(models.Model):
	name=models.CharField(max_length=100)
	company=models.CharField(max_length=200)
	role=models.TextField()
	start_date=models.DateTimeField()
	end_date=models.DateTimeField()

	class Meta:
		ordering=['-start_date']

	def __str__(self):
		return self.name

class About(models.Model):
	descr=models.TextField()

	def __str__(self):
		return self.descr

class Project(models.Model):
	name=models.CharField(max_length=100)
	descr=models.TextField()
	link=models.TextField()
	image=models.ImageField(upload_to='images/')

	def __str__(self):
		return self.name

class Messages(models.Model):
	text=models.TextField(max_length=100)
	email=models.CharField(max_length=255)
	created_on=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text