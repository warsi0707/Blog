from django.shortcuts import render, HttpResponse, redirect
from myblog.models import Post, BlogComment
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def blogpage(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,"myblog/blogpage.html", context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    context = {'post':post, 'comments':comments, 'user':request.user}
    return render(request,"myblog/blogPost.html", context)

def postcomment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.User
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        comments=BlogComment(comment=comment, user=user, post=post)
        comments.save()
        messages.success(request, "Your comment has been posted successfully")
    return redirect({post.slug})