from django import forms
from .models import UserProfile, Post, Comment
# these are already given to us 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import Textarea, CheckboxInput


# form used to register a user
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("first_name","username", "email", "password1", "password2")


# form used to create and edit a post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "link",
            "content",
        ]
        widgets = {
            # this sets the input text area
            "content": Textarea(attrs={"cols": 60, "rows": 10}),
            # "slug": forms.HiddenInput()
        }

# form used to create and edit a comment
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




