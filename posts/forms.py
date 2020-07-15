from django import forms
from posts.models import BlogPost

class BlogPostForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = '__all__'
		exclude = ['read','author',]