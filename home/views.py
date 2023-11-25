from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, reverse, redirect, HttpResponse
from home.models import Contact
from django.contrib import messages
from myblog.models import Post

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email) <5 or len(phone)<10  or len(content)<10 :
            messages.error(request, "Please fill the form correctly!")
        else:
            contact = Contact(
            name=name,
            email=email,
            phone=phone,
            content=content,
            )
            contact.save()
            messages.success(request,"Your response has been submitted successfully!")
    return render(request, "home/contact.html")

def about(request):
    return render(request, "home/about.html")

def search(request):
    query = request.GET['query']
    if len (query)> 70:
        allpost = Post.objects.none()
    else:
        allpost = Post.objects.filter(title__icontains=query)
        allpost = Post.objects.filter(author__icontains=query)
        allpost = Post.objects.filter(content__icontains=query)

    if allpost.count() == 0:
        messages.warning(request,"No search found! please re-search ")
    
    output={'allpost':allpost}
    return render(request,'home/search.html', output)


def signup(request):
    if request.method == 'POST':

        # PARAMETER
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #Check for error in the input
        if len(username)>10:
            messages.error(request, "Ussername should be less than 10 characters.")
            return redirect('homepageHome')
        if (password1 != password2):
            messages.error(request, "Confirm password didn't match with password")
            return redirect('homepageHome')

        #Creating User 
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your account has been created succesfully")
        return redirect('homepageHome')

    else:
        return HttpResponse("Error! - Please try again")



def login(request):
    if request.method == 'POST':
        #Pareameter for the post
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username = username, password1 = password1)
        if user is not None:
            messages.error(request, "Invalid credentials! Please check and retry")
            return redirect('homepageHome')

        else:
            login(request, user)
            messages.success(request,"Successfully logged In")
            return redirect('homepageHome')
    return HttpResponse("Error! 404 - Not Found!")

def logout(request):
    logout(request)
    messages.success(request,"Successfully logged Out! ")
    return redirect('homepageHome')