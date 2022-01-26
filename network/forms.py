from django import forms
from .models import User


class CreatePostForm(forms.Form):
    contents =forms.CharField(label="",required= False, widget= forms.Textarea
    (attrs={'placeholder':'What\'s happening?','class':'col-sm','style':'top:1rem,margin:10rem'}))

class EditPostForm(forms.Form):
    contents =forms.CharField(label="",required= False, widget= forms.Textarea
    (attrs={'class':'col-sm','style':'top:1rem,margin:10rem'}))

class FollowForm(forms.Form):
    btn = forms.CharField()
    change = forms.IntegerField()
    fromSection = forms.CharField(required= False)