from django import forms
from django.forms import ModelForm
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='User name',widget=forms.TextInput(attrs={'class':'form-control','id':'floatingInput','placeholder':'User name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','id':'floatingPassword','placeholder':'Password'}))
  
  
class RegistartionForm(ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'floatingPassword'}))
    confirm_password = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'floatingPassword'}))
    
    def set_up(self):       
        self.fields['username'].label= 'User name'
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['placeholder'] = i.field.label

    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
class UserForm(ModelForm):   
    
    
    def set_up(self):        
        self.fields['username'].label= 'User name'
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['placeholder'] = i.field.label
            
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
    
class ResetPasswordForm(forms.Form):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'password'}))
    confirm_password = forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'confirmPass'}))
            