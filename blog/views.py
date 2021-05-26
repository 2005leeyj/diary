from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def first(request):
    blogs = Blog.objects.all ()
    count = Blog.objects.all().count()
    return render(request, 'first.html', {'blogs':blogs, 'count':count})

@login_required(login_url='/account/login/')
def home(request):
    blogs = Blog.objects.all ()
    return render(request,'home.html',{'blogs':blogs})

@login_required(login_url='/account/login/')
def detail(request, id):
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog':blog})

@login_required(login_url='/account/login/')
def new(request):
    form = BlogForm()
    return render(request, 'new.html',{'form':form})

@login_required(login_url='/account/login/')
def create(request):
    form = BlogForm(request.POST, request.FILES)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.pud_date = timezone.now()
        new_blog.save()
        return redirect ('detail',new_blog.id)
    return redirect('first')

@login_required(login_url='/account/login/')
def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html',{'blog':edit_blog})

@login_required(login_url='/account/login/')
def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pud_date = timezone.now()
    update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect ('detail',update_blog.id)    

@login_required(login_url='/account/login/')
def delete(request, id):
  delete_blog = Blog.objects.get(id= id)
  delete_blog.delete()
  return redirect('home')
