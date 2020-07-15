from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import datetime

# Create your views here.
def index(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=7)
    trends = BlogPost.objects.filter(pub_date__gte=week_ago).order_by('-read')
    return render(request, 'index.html', {'trends':trends[:6]})

def blogs(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 6)
    page = request.GET.get("pg")
    posts = paginator.get_page(page)
    return render(request, 'blogs.html', {'posts':posts})

@login_required
def blogPost(request, id):
    post = BlogPost.objects.get(pk=id)
    post.read += 1
    post.save()
    params = {'post':post}
    return render(request, 'blogpost.html',params)

@login_required
def addPost(request):
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                # form.save(commit=False).manage = request.user    #here we are associating the saved form to logged in user 
                # form.save()
                obj = form.save(commit=False)
                obj.author = request.user
                obj.save()
                messages.success(request, "Blog added successfully")
                return redirect('blogs')
            else:
                messages.info(request, "Please login to add blog post")        
            
        else:
            messages.error(request, "Title should be unique and image format should be valid")
            form = BlogPostForm()

    else:
        form = BlogPostForm()
    return render(request, 'addpost.html', {'form':form})

@login_required
def editPost(request, id):
    post = BlogPost.objects.get(pk=id)
    if request.method == "POST":
        form = BlogPostForm(data=request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            if request.user.is_authenticated:
                if request.user == post.author:
                    form.save()
                    messages.success(request, "Blog edited successfully")
                else:
                    messages.success(request, "You are not authorized to edit this blog")
                return redirect('blogs')
            else:
                messages.info(request, "Please login to edit blog post")
        else:
            messages.info(request, "Title should be unique and image should be of valid format")
            form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'addpost.html', {'form':form})

def search(request):
    if "q" in request.GET and request.GET["q"]:
        query =  request.GET["q"]
        searchQuery = BlogPost.objects.filter(Q(title__icontains=query)|Q(author__username__icontains=query)|Q(head0__icontains=query)|Q(chead0__icontains=query)|
        Q(head1__icontains=query)|Q(chead1__contains=query)|Q(about__contains=query))
        if len(searchQuery) >= 1:
            return render(request, 'searchpost.html', {'searchQuery':searchQuery})
        else:
            messages.info(request, "No item matches with your search query")
            return redirect('index')
    else:
        messages.info(request, "Please enter a valid search query")
        return redirect('index')
        

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')