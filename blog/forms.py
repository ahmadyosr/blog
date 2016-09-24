from django import forms
from django.db import models
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
	class Meta:
		model=BlogPost
		fields = '__all__'
