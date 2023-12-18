from django import forms

from .models import polls

class pollsForm(forms.ModelForm):

	class Meta:
		model = polls
		fields = ("usuario", "senha")

