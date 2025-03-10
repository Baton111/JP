from django import forms
class PostForm(forms.Form):
    skills =  forms.CharField(max_length=255)

