from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from  .models import Theme, Individual_Post

from .forms import BlogForm, PostForm
# Create your views here.

def mainpage(request):
    all_theme = Individual_Post.objects.order_by("-date_added")
    context = {"all_theme": all_theme}
    return render(request, 'blogs/mainpage.html', context)

@login_required
def making_blog(request):
    if request.method != "POST":
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:mainpage')
    context = {"form": form}
    return render(request, 'blogs/making_blog.html', context)

@login_required
def making_post(request):
    # blog = Theme.objects.get(id=blog_id)

    if request.method != "POST":
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:mainpage')
    context = {'form': form}

    return render(request, 'blogs/making_post.html', context)

@login_required
def editing_post(request, post_id):

    post = Individual_Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:mainpage')
        
    context = {'form': form, 'post': post}
    return render(request, 'blogs/editing_post.html', context)