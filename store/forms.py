from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import(AbstractBaseUser)
from .models import Customer
#01097073808

class LoginReg(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class': 'btn btn-1 '}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    # phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    # password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'btn btn-1', 'placeholder': 'Password ','help_text':"HI HELL\n"}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone','password1','password2')
        # subject = forms.CharField(label='subject', max_length=100,widget=forms.TextInput(attrs={'class': "form-control"}))   
        # labels={
        #     "username": " username",
        # }
        # error_messages=""
    
    def __init__(self,*args,**kwargs):
        super(LoginReg,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = "btn btn-1 "
        self.fields['username'].help_text = ""
        self.fields['username']. errorlist=""
        # self.fields['username'].errors = "a"
        # self.fields['password1'].help_text = "make sure u r secure with us "
        self.fields['password1'].widget.attrs['class'] = "btn btn-1 btn-2 "
        self.fields['password1'].help_text = ""
        # self.fields['password1'].help_text = mark_safe(_(
        #     f'<small style="color:var(--cls-neon)">{self.fields["password1"].help_text}</small>'
        # )) 
   

  
        self.fields['password2'].widget.attrs['class'] = "btn btn-1 "
        self.fields['password2'].help_text = ""
        
class Update_user_form(UserChangeForm):
    #HIDE PASSWORD 
    password = None
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class': 'btn btn-1 '}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    # phone = models.ForeignKey(Customer,on_delete=models.CASCADE,max_length=100,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone')

    def __init__(self,*args,**kwargs):
        super(Update_user_form,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = "btn btn-1 "
        #for f in self.fields.values():
        #    f.widget.attrs['disabled'] =True

        self.fields['username'].help_text = ""
        # self.fields['password1'].help_text = "make sure u r secure with us "
        # self.fields['password1'].widget.attrs['class'] = "btn btn-1 "
        # self.fields['password2'].widget.attrs['class'] = "btn btn-1 "

class Change_p(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1','new_password2']
    def __init__(self,*args,**kwargs):
        super(Change_p,self).__init__(*args,**kwargs)
        self.fields['new_password1'].widget.attrs['class'] = "btn btn-1 "
        self.fields['new_password1'].help_text = ""
        self.fields['new_password2'].widget.attrs['class'] = "btn btn-1 "
        self.fields['new_password2'].help_text = ""