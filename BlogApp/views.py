from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.contrib import messages

from .models import *
from .forms import *

from django.core.paginator import Paginator,EmptyPage
# Create your views here.


CATEGORY = ['All','Technology', 'Fashion', 'Nature', 'Food', 'Travel', 'Music', 'Lifestyle', 'Fitness', 'DIY', 'Sports', 'Finance', 'Political', 'Parenting', 'Business', 'Personal', 'Movie', 'Automobile', 'News', 'Pet', 'Gaming', 'Other']

@csrf_exempt
def home(request):
	obj = Blog.objects.all().order_by('dateCreated').reverse()

	if request.method=="POST":
		subs = request.POST.get('Subscribe')
		if subs:
			try:
				subsObj = Subscribers(email=subs)
				subsObj.save()


				html_content = render_to_string("email_subscribe.html")
				text_content = strip_tags(html_content)

				subject = 'Subscribed to Blog-A-ware'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [subs, ]
				#send_mail( subject, message, email_from, recipient_list )
				email = EmailMultiAlternatives(
					subject,text_content,
					email_from,recipient_list
					)
				email.attach_alternative(html_content,"text/html")
				email.send()

				messages.info(request,str(subs)+" subscribed")
			except:
				messages.info(request,str(subs)+" already subscribed")
		else:
			category = request.POST.get('category')
			if category != 'All':
				obj = Blog.objects.filter(category=category).order_by('dateCreated').reverse()

	null=False if obj else True
	global CATEGORY

	p = Paginator(obj,6)
	pList = list(range(1,p.num_pages+1))
	page_num = request.GET.get('page',1)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {'Blogs':page,'category':CATEGORY,'null':null,'Pages':pList}

	if request.user.is_authenticated:

		context['total'] = request.user.blog_set.count()
		try:
			l= max(request.user.blog_set.all(),key=lambda x:x.likes.count())
			context['likes'] = l
		except:
			context['likes'] = False
	return render(request,'index.html',context)



@csrf_exempt
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		frm = CreateUserForm()

		if request.method == "POST":
			frm = CreateUserForm(request.POST)

			if frm.is_valid():
				frm.save()
				user = frm.cleaned_data.get('username')
				emailId = frm.cleaned_data.get('email')
				messages.success(request,'Account created for : ' + user+"\n Log in Now !")


				html_content = render_to_string("email_welcome.html")
				text_content = strip_tags(html_content)

				subject = 'Welcome to Blog-A-ware'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [emailId, ]
				#send_mail( subject, message, email_from, recipient_list )
				email = EmailMultiAlternatives(
					subject,text_content,
					email_from,recipient_list
					)
				email.attach_alternative(html_content,"text/html")
				email.send()

				subsObj = Subscribers(email=emailId)
				subsObj.save()

				#messages.info(request,"Login with Registed Username!")
				return redirect('login')

		return render(request,'register.html',{'form':frm})



@csrf_exempt
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == "POST":
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request,username=username, password=password)

			if user:
				login(request,user)
				messages.success(request,'Welcome '+username+' !')
				return redirect('home')
			else:
				messages.success(request,'Incorrect Username or Password !')
				return render(request,'login.html')

		return render(request, 'login.html')



@login_required(login_url='login')
def logoutUser(request):
	logout(request)
	messages.info(request,'You have been logged Out!')
	return redirect('home')



@csrf_exempt
@login_required(login_url='login')
def writeBlog(request):
	frm = BlogForm()

	if request.method == "POST":
		a = request.user
		b = request.POST.get("title")
		c = request.POST.get("category")
		d = request.POST.get("content")
		e = request.POST.get("references")
		f = request.FILES.get("image")
		g = request.POST.get("description")
		obj = Blog(user=a,title=b,category=c,content=d,references=e,image=f,description=g)
		obj.save()

		messages.info(request,"Yay! New Blog Added")

		subsObj = set(Subscribers.objects.filter().values_list('email', flat=True))


		blogLink = "https://blogaware.herokuapp.com/read/"+str(obj.id)
		html_content = render_to_string("email_blog.html",{"ecategory":c,"etitle":b,"eauthor":a.username,"elink":blogLink,"edesc":g})
		text_content = strip_tags(html_content)

		subject = 'New Blog in the house'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = list(subsObj)
		#send_mail( subject, message, email_from, recipient_list )
		email = EmailMultiAlternatives(
			subject,text_content,
			email_from,recipient_list
			)
		email.attach_alternative(html_content,"text/html")
		email.send()

		return redirect('home')

	context ={'form':frm}
	return render(request,'write.html',context)

@csrf_exempt
@login_required(login_url='login')
def updateBlog(request,pk):
	obj = request.user.blog_set.get(id=pk)
	im = obj.image
	form = BlogForm(instance = obj)


	if request.method=="POST":
		obj.title=request.POST.get("title")
		obj.category=request.POST.get("category")
		obj.content=request.POST.get("content")
		obj.references=request.POST.get("references")
		obj.description=request.POST.get("description")
		if request.FILES.get("image"):
		    obj.image=request.FILES.get("image")
		else:
		    obj.image=im
		obj.save()
		messages.info(request,"Blog Updated")
		return redirect('myblogs')

	context={'form':form,'obj':obj}
	return render(request,'write.html',context)

@csrf_exempt
@login_required(login_url='login')
def deleteBlog(request,pk):
	obj = Blog.objects.get(id=pk)
	if request.method == "POST":
		obj.delete()
		messages.info(request,"Blog deleted.")
		return redirect('myblogs')

	context = {"Blog":obj}
	return render(request,'delete.html',context)




@login_required(login_url='login')
def myBlogs(request):
	obj = request.user.blog_set.all().order_by('dateCreated').reverse()

	p = Paginator(obj,6)
	pList = list(range(1,p.num_pages+1))
	page_num = request.GET.get('page',1)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)



	context = {'Blogs':page,'Pages':pList}
	return render(request,'myblogs.html',context)


def readBlog(request,pk):
	obj = Blog.objects.get(id=pk)
	url = "images/default/"+str(obj.category)+".jpg"

	context = {"Blog":obj,"Liked":False,"url":url}
	if obj.likes.filter(id=request.user.id).exists():
		context['Liked']=True

	return render(request,'post.html',context)

def showProfile(request,pk):
	obj = User.objects.get(username=pk)

	context = {'obj':obj}


	context['total'] = obj.blog_set.count()
	try:
		l= max(obj.blog_set.all(),key=lambda x:x.likes.count())
		context['likes'] = l
	except:
		context['likes'] = False

	return render(request,'profile.html',context)



def BlogPostLike(request, pk):
    post = Blog.objects.get(id=pk)

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        messages.success(request,"Blog Unliked")
    else:
        post.likes.add(request.user)
        messages.success(request,"Blog Liked")

    post.save()
    return HttpResponseRedirect(reverse('read', args=[str(pk)]))


@login_required(login_url='login')
def likedBlogs(request):
	obj = Blog.objects.filter(likes= request.user).order_by('dateCreated').reverse()

	p = Paginator(obj,6)
	pList = list(range(1,p.num_pages+1))
	page_num = request.GET.get('page',1)
	try:
		page = p.page(page_num)
	except EmptyPage:
		page = p.page(1)

	context = {'Blogs':page,'Pages':pList}
	return render(request,'likedblogs.html',context)


@csrf_exempt
@login_required(login_url='login')
def updateProfile(request):
	obj = Author.objects.get(user=request.user)
	im = obj.picture
	frm = ProfileForm(instance=obj)

	if request.method=="POST":
		obj.picture = request.FILES.get("picture") if request.FILES.get("picture") else im
		obj.description = request.POST.get("description")
		obj.linkedin = request.POST.get("linkedin")
		obj.facebook = request.POST.get("facebook")
		obj.twitter = request.POST.get("twitter")
		obj.github = request.POST.get("github")
		obj.instagram = request.POST.get("instagram")
		obj.youtube = request.POST.get("youtube")

		messages.info(request,"Profile Updated")
		obj.save()

		return HttpResponseRedirect(reverse('profile', args=[str(request.user.username)]))

	context={'form':frm,'obj':obj}
	return render(request,'updateprofile.html',context)

def RespectiveBlogs(request,pk):
	u = User.objects.get(username=pk)
	obj = u.blog_set.all().order_by('dateCreated').reverse()



	context = {'Blogs':obj,"Author":u,}
	return render(request,'respectiveblogs.html',context)


@csrf_exempt
def unsubscribe(request):

	if request.method == "POST":
		mailId = request.POST.get("email")
		print(mailId)
		obj = None
		try :
			obj = Subscribers.objects.get(email = mailId)
			messages.info(request,str(mailId)+" Unsubscribed!")
		except:
			messages.info(request,"Mail Id Not in Record.")


		if obj :
			obj.delete()

			html_content = render_to_string("email_unsubscribe.html")
			text_content = strip_tags(html_content)
			subject = 'Unsubscribed from Blog-a-ware'

			email_from = settings.EMAIL_HOST_USER
			recipient_list = [mailId,]
			email = EmailMultiAlternatives(subject,text_content,email_from,recipient_list)
			email.attach_alternative(html_content,"text/html")
			email.send()

    		#send_mail( subject, message, email_from, recipient_list )




			return redirect("home")

	return render(request,"unsubscribe.html")



def  email(request):
	return render(request,"email_welcome.html",{"ecategory":"Technology","etitle":"Binomial Theorem","eauthor":"deeware"})
