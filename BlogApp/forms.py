from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#from djrichtextfield.widgets import RichTextWidget
from ckeditor.widgets import CKEditorWidget

from .models import * 

# Both these Classes will allow capturing date & time in HTML5 way

class CreateUserForm(UserCreationForm):

	password1 = forms.CharField(label="Password",
		widget=forms.PasswordInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none', 'type':'password', 'align':'center', 'placeholder':'Password...'}))
	password2 = forms.CharField(label="Confirm Password",
		widget=forms.PasswordInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none', 'type':'password', 'align':'center', 'placeholder':'Confirm Password...'}))
    
	class Meta:
		model = User
		fields = ['username','email']
		widgets = {
            'username': forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'Username...'}),
            'email': forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'Email...'}),
        }
		
		
class BlogForm(forms.ModelForm):
	
	class Meta :
		model = Blog
		content = forms.CharField(widget=CKEditorWidget(attrs={'placeholder':'Maximize ✥ for ease of writing'}))
		content.widget.field_settings = {'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','style':"width:80%;",'settings': True,'placeholder':'Maximize ✥ for ease of writing'}
		fields = ['title','category','description','content','references','image']
		widgets = {
		'title':forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none font-bold','placeholder':'Technology : A ban or boon','autofocus':'','style':"width:100%;"}),
		'category':forms.Select(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','style':"width:100%;"}),
		'description':forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','style':"width:100%;",'placeholder':"A one line description..."}),
		'content':forms.Textarea(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','style':"width:100%;"}),
		'references':forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','style':"width:100%;"}),
		
		}
	class Media :
		css = {
		'all' : ("https://unpkg.com/tailwindcss/dist/tailwind.min.css",)
		}


class ProfileForm(forms.ModelForm):
	
	class Meta:
		model=Author
		fields = '__all__'
		exclude =['user']
		widgets = {
		'description' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'Totally optional short description about yourself','autofocus':'','style':"width:80%;"}),
		'linkedin' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'https://www.linkedin.com/....','autofocus':'','style':"width:80%;"}),
		'facebook' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'http://www.facebook.com/....','autofocus':'','style':"width:80%;"}),
		'twitter' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'http://twitter.com/....','autofocus':'','style':"width:80%;"}),
		'github' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'https://github.com/....','autofocus':'','style':"width:80%;"}),
		'instagram' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'https://www.instagram.com/....','autofocus':'','style':"width:80%;"}),
		'youtube' : forms.TextInput(attrs={'class':'flex-1 appearance-none rounded shadow p-3 text-gray-600 mr-2 focus:outline-none','placeholder':'https://youtube.com/....','autofocus':'','style':"width:80%;"}),

		}


