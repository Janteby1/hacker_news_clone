from django import forms
from .models import UserProfile, Post, Comment
# these are already given to us 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("first_name","username", "email", "password1", "password2")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "link",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 60, "rows": 10}),
            # "slug": forms.HiddenInput()
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "title",
            "link",
            "content",
        ]
        widgets = {
            "content": Textarea(attrs={"cols": 30, "rows": 5})
        }




