from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, HttpResponseForbidden

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #fancy decorator
from django.contrib.auth.models import User

from .forms import UserForm, PostForm, CommentForm
from .models import UserProfile, Post, Comment
import pudb

import json
from django.http import JsonResponse


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
        comments = Comment.objects.all().order_by('-created_at')
        # put al the posts and commentss into a context dict
        context ["posts"] = posts
        context ["comments"] = comments
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
            # if there is no user logged in they can not submit a post 
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


class Edit_Post(View):
    template = "edit.html"

    # here we get the slug id passed in with the url 
    def get(self, request, post_slug=None):
        # get the slug id from the object
        post = Post.objects.get(slug=post_slug)
        # get the form and populate it with the value that is already there, AKA what we want ot edit
        form = PostForm(instance=post)
        # send the comment form also
        comment_form = CommentForm()
        context = {
            "post": post,
            "EditForm": form,
            "CommentForm": comment_form}
        return render(request, self.template, context)


    def post(self, request, post_slug=None):
        # get the slug id from the object
        post = Post.objects.get(slug=post_slug) # dont need this line 
        # this time we get the NEW, EDITED content from the form 
        form = PostForm(data=request.POST, instance=post)

        if form.is_valid():
            # if the form is valid we save it to the db
            form.save()
            return redirect("news:index")
        else:
            context = {
                "post": post,
                "EditForm": form,}
            # if it is not valid just send it back with the errors attached
            return render(request, self.template, context)


class Delete_Post(View):
    # dont need a get just get the slug id and change the value for show
    def post(self, request, post_slug=None):

        post = Post.objects.get(slug=post_slug)
        # dont delte it just make the show field false so it wont show on index page
        post.show = False
        post.save()
        return redirect('news:index')



class Add_Comment(View):
    template = "edit.html"

    def get(self, request):
        pass
        # we already rendered the form in our edit class view

    def post(self, request, post_slug=None):
        if not request.user.is_authenticated():
            # if there is no user logged in they can not submit a comment 
            # this redirects them to a 403 html page with an error message
            return HttpResponseForbidden(render (request, "403.html"))

        # get the jason object with the data
        # value = json.loads(request.body.decode("utf-8")) 

        form = CommentForm(request.POST)
        # # if the form is valid then we...
        if form.is_valid():

            # need to save the user and post id to this comment
            user = request.user
            post = Post.objects.get(slug=post_slug)
            comment = form.save(commit=False)
            # save the user and post to this specific comment, AKA add an FK
            comment.user = user
            comment.post = post
            comment.save()
            # return redirect("news:index") 

            message={
                'comment': request.POST.get("content") }
            return JsonResponse(message) # return a json object

        else:
            context = {
                "CommentForm": form,}
            # send the form back with errors
            return render(request, self.template, context)



# Edit / delete a comment 
class Edit_Comment(View):
    template = "edit_comment.html"

    # here we get the slug id passed in with the url 
    def get(self, request, comment_slug=None):
        # get the slug id from the object
        comment = Comment.objects.get(slug=comment_slug)
        # get the form and populate it with the value that is already there, AKA what we want ot edit
        form = CommentForm(instance=post)
        # send the comment form also
        context = {
            "post": post,
            "CommentForm": comment_form}
        return render(request, self.template, context)


    def post(self, request, comment_slug=None):
        # get the slug id from the object
        comment = Comment.objects.get(slug=comment_slug)  
        # this time we get the NEW, EDITED content from the form 
        form = CommentForm(data=request.POST, instance=post)

        if form.is_valid():
            # if the form is valid we save it to the db
            form.save()
            return redirect("news:index")
        else:
            context = {
                "post": post,
                "CommentForm": form,}
            # if it is not valid just send it back with the errors attached
            return render(request, self.template, context)


class Delete_Comment(View):
    # dont need a get just get the slug id and change the value for show
    def post(self, request, comment_slug=None):

        comment = Comment.objects.get(slug=comment_slug)
        # dont delte it just make the show field false so it wont show on index page
        comment.show = False
        comment.save()
        return redirect('news:index')




# add user constraints - only edit or delte something you created





