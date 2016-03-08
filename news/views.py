from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #fancy decorator
from django.contrib.auth.models import User

from .forms import UserForm, PostForm, CommentForm
from .models import UserProfile, Post, Comment
import pudb


# Create your views here.
class Index(View):
    def get(self, request):
        # create blank conext incase someone isnt signed in already 
        context = {}
        # check to see if someone is already logged in
        if request.user.is_authenticated(): 
            # get their username  
            username = request.user.username
            message = ("Hello, " + username)
            context = {
                'message': message,}
        # this line gets all the posts that we have in the db and orders them by most recent
        posts = Post.objects.all().order_by('-updated_at')
        # put al the posts into a context dict
        context ["posts"] = posts
        # send them all to the template
        return render(request, "index.html", context)


class User_Register(View):
    # pu.db
    template = "register.html"

    def get(self, request):
        "get the user form from forms.py and send it to the template in the context"
        user_form = UserForm()
        context = {
            'user_form': user_form,}
        return render(request, self.template, context)

    def post(self, request):
        user_form = UserForm(data=request.POST)
        # If the form is valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.save()
            # return render(request, "blog/index.html", {})
            return redirect("news:index")

        else:
            context = {
                'user_form': user_form,}
            # send the form back with errors atatched 
            return render(request, self.template, context)


class User_Login(View):
    template = "login.html"

    def get(self, request):
        # if the user is already signed in 
        if request.user.is_authenticated():
            return redirect("news:index")
        return render(request, self.template, {})

    def post(self, request):
        # Gather the username and password entered by the user.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's to see if the username/password combination is valid, returns user object
        user = authenticate(username=username, password=password)

        if user: # meaning it is not None
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                login(request, user) 
                # send them back to the index and show them as logged in there
                return redirect("news:index")
            else:
                # An inactive account was used
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided
            # print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")


class User_Logout(View):
    # Use the login_required() decorator to ensure only those logged in can access the view.
    # @login_required
    def get(self, request):
        # Since we know the user is logged in, we can now just log them out.
        logout(request)
        # Take the user back to the homepage.
        return redirect("news:index")


class Create_Post(View):
    template = "create.html"

    def get(self, request):
        form = PostForm()
        # set the form and send it to the page 
        context = {
            "PostForm": form}
        return render (request, self.template, context)

    def post(self, request):
        if not request.user.is_authenticated():
            # is there is no user logged in they can not submit a post 
            # this redirects them to a 403 html page with an error message
            return HttpResponseForbidden(render (request, "403.html"))

        form = PostForm(data=request.POST)
        # if the form is valid hen we...
        if form.is_valid():
            # need to save the username the post is attached to
            user = request.user
            post = form.save(commit=False)
            # save the user to this specific post, AKA add an FK
            post.user = user 
            post.save()
            return redirect("news:index")

        else:
            context = {
                "PostForm": form,}
            # send the form back with errors
            return render(request, self.template, context)

















