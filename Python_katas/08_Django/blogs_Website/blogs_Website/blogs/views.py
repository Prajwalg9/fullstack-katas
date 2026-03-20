from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog, Author, Tag, Comment
from .forms import CommentForm, RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    blogs=Blog.objects.all().order_by('-date')
    return render(request, 'blogs/index.html', {'blogs': blogs, })

@login_required
def post_detail(request, blog):
    blog_post = get_object_or_404(Blog, title=blog)
    comments=Comment.objects.filter(blog=blog_post).order_by('-id')
    if request.method=='POST':
        formdata=CommentForm(request.POST)
        if formdata.is_valid():
            new_comment=formdata.save(commit=False)
            new_comment.blog = blog_post
            new_comment.user_name = request.user.username
            new_comment.user_email = request.user.email
            new_comment.save()
            messages.success(request, 'Your comment has been added.')
            return redirect('post_detail',blog=blog_post.title)
        else:
            messages.error(request, 'Please correct the comment.')
    else:
        formdata=CommentForm()
    return render(request, 'blogs/post.html', {'blog': blog_post, 'formdata': formdata, 'comments': comments})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the form.')
    else:
        form = RegisterForm()
    return render(request, 'Authentication/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'Authentication/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')