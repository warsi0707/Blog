from django.shortcuts import render, HttpResponse
from myblog.models import Post

# Create your views here.
def blogpage(request):
    allpost = Post.objects.all()
    context = {'allpost':allpost}
    return render(request,"myblog/blogpage.html", context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,"myblog/blogPost.html", context)