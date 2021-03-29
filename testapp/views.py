from django.shortcuts import render,get_object_or_404,redirect
from testapp.models import Post,Comment
from django.contrib.auth.models import User,auth
from ecomwebsite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from .forms import CommentForm
# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

def index_view(request):
    if request.method=='POST':
        name=request.POST['name']
        print(name)
    return render(request,'index.html')

def tracker_view(request):
    return render(request,'tracker.html')

def search_view(request):
    return render(request,'search.html')


def productview_view(request,product_name):
    #post=get_object_or_404(Post,product_name=product_name)
    post=Post.objects.get(product_name=product_name)

    comments = post.comments.filter(active=True)
    csubmit=False
    # Comment posted
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            csubmit=True
    else:
        form = CommentForm()
    return render(request,'productview.html',{'product':post,'comments': comments,
                                           
                                           'form': form,
                                           })

def checkout_view(request):
    return render(request,'checkout.html')

def order_view(request):
    return render(request,'order.html')

def gold_view(request):
    product=product_model.objects.all()
    return render(request,'gold.html',{'product':product})

def silver_view(request):
    if "search" in request.GET:
        search=request.GET['search']
        product=Post.objects.filter(product_name__icontains=search)|Post.objects.filter(price__icontains=search)
        #product=Post.objects.filter(price__icontains=search)
        
    else:
        product=Post.objects.all()

    
    return render(request,'silver.html',{'product':product})

def signup_view(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['re_password']
        
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect("/login")
    return render(request,'signup.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/index")
        else:
            return redirect("/login")
    return render(request,'login.html')

def filter_view(request):
    return render(request,'filter.html')

def zerotohundred(request):
    product=Post.objects.filter(price__lte=100)

    return render(request,'0to100.html',{'product':product})

def hundredtothreehun(request):
    product=Post.objects.filter(price__gte=101)

    return render(request,'100to300.html',{'product':product})


def mail_view(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email)
        # subject="client {} place an order".format(cd['name'])
        # message="{} placed an order on {} and her contact no is :{}".format(cd['name'],cd['nameofproduct'],cd['phoneno'])
        # send_mail(subject,message,cd['senderemail'],['krishna.django@gmail.com'])
        # return redirect("/thank")
    return render(request,'index.html')