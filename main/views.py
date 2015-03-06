from django import forms
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from main.models import Post, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


class Posts(View):
    def get(self, request):
        posts = Post.objects.filter(publish=True).order_by('-when')
        return HttpResponse(render(request, 'posts.html', {'posts': posts}))


class Login(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('No such login/password')


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class AddPost(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponse(render(request, 'edit_post.html', {}))
        else:
            return HttpResponseRedirect('/')

    def post(self, request):
        header = request.POST['header']
        content = request.POST['content']
        publish = 'publish' in request.POST
        Post.objects.create(header=header, text=content, publish=publish)
        return HttpResponseRedirect('/')


class SinglePost(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=post).order_by('when')
        return HttpResponse(render(request, 'single_post.html', {'post': post, 'comments': comments}))


class EditPost(View):
    def get(self, request, id):
        if not request.user.is_authenticated():
            return HttpResponseRedirect('/posts/{}/'.format(id))

        post = Post.objects.get(id=id)
        return HttpResponse(render(request, 'edit_post.html', {'post': post}))

    def post(self, request, id):
        post = Post.objects.get(id=id)
        header = request.POST['header']
        content = request.POST['content']
        publish = 'publish' in request.POST
        post.header = header
        post.text = content
        post.publish = publish
        post.save()
        return HttpResponseRedirect('/posts/{}/'.format(id))


class AddComment(View):
    def post(self, request, id):
        comment = request.POST['comment']
        post = Post.objects.get(id=id)
        who = request.user
        Comment.objects.create(text=comment, post=post, who=who)
        return HttpResponseRedirect('/posts/{}/'.format(id))


class About(View):
    def get(self, request):
        return HttpResponse(render(request, 'about.html', {}))


class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        form = UserCreationForm()
        return render(request, "registration/register.html", {
            'form': form,
        })

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
        return render(request, "registration/register.html", {
            'form': form,
        })


