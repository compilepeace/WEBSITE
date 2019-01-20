from django import forms
from .models import Post


# Create a form named 'PostForm' which is a Model-Form
class PostForm(forms.ModelForm):

	# Class that tells 'Post' model should be used to create the form
	class Meta:
		model = Post
		fields = ('title', 'text',)
