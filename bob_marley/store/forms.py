from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
#01097073808

class LoginReg(UserCreationForm):
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={'class': 'btn btn-1 '}))
    phone = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'btn btn-1'}))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone','password1','password2')

    def __init__(self,*args,**kwargs):
        super(LoginReg,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = "btn btn-1 "
        self.fields['password1'].help_text = "make sure u r secure with us "
        self.fields['password1'].widget.attrs['class'] = "btn btn-1 "
        self.fields['password2'].widget.attrs['class'] = "btn btn-1 "
        
        
