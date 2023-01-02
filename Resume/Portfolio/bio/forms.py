from django.forms.models import ModelForm
from .models import Messages

class MessageForm(ModelForm):
	class Meta:
		model=Messages
		fields=['text','email']