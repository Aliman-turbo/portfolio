# from  django import forms
# from .models import User,Message
#
#
# class User_form(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['name']
#         widgets = {'name':forms.TextInput(attrs={'class':'form-control','placehplder':'Enter your name'})}
# class Message_form(forms.ModelForm):
#     class Meta:
#         model = Message
#         fields = ['text']
#         widgets = {'text': forms.TextInput(attrs={'class': 'form-control', 'placehplder': 'Enter your message''rows:3'})}
from django import forms
from .models import User, Message

class User_form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            })
        }

class Message_form(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your message',
                'rows':3
            })
        }
class MessageEditForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Edit your message','rows':3
            })
        }