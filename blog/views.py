from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
@login_required
def index(request):
	blog_posts = BlogPost.objects.all()
	return render(request,'blog/index.html',{'blog_posts':blog_posts })
	
def new_post(request):
	if request.method == 'POST':
		form=BlogPostForm(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.save()
		return redirect('index')
	else:
		form=BlogPostForm()
	return render(request,'blog/new_post.html',{'form':form})