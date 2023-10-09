from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
  
  posts = Post.objects.order_by('-date')
  return render(request,'myApp/home.html',{
    "posts":posts
    
  })


def signin_view(request):
  
  form = UserCreationForm()
  if request.method == "POST":
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, 'myApp/login.html', {
                "message": "Signed in successfully! please Log in."
            })
  return render(request, 'myApp/signin.html', {
        "form": form
    })


def login_view(request):

  
  if request.method == "POST":

    username = request.POST['username']

    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('index')
    else:
      return render(request, 'myApp/login.html', {
                "message": "Invalid Data!"
            })
  else:
    return render(request, 'myApp/login.html')

def logout_view(request):
  logout(request)
  return HttpResponseRedirect(reverse(index))

@login_required
def createPost(request):
  if request.method == "GET":
        return render(request,'myApp/create.html')
  else:
            #get the data
        title= request.POST["title"]
        
        
        content = request.POST["content"]
        date = request.POST["date"]
        #the user
        
        #get the content of category
        
        #creat bid
        newPost = Post( owner=request.user, title= title, content=content, date=date)
        newPost.save()
        
        #create new listing
        
        return HttpResponseRedirect(reverse(index))
  
def filterPost(request):
  Allposts = Post.objects.filter(owner=request.user)
  posts = Allposts.order_by('-date')
  return render(request,'myApp/home.html',{
    "posts":posts
    
  })
  
  
def postDetails(request, id):
  post = Post.objects.get(pk=id)
  comments= Comment.objects.filter(post=post)
  return render (request, "myApp/details.html",{
    "post":post,
    "comments":comments
        
    })
  
  
def addComment(request, id):
  post = Post.objects.get(pk=id)
  author = request.user
  message = request.POST['newComment']
  newComment= Comment(author=author, message=message, post=post)
  newComment.save()
  return HttpResponseRedirect(reverse(postDetails, args=(id, )))