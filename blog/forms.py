from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'text',)

#registration form
class Registration(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(Registration, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class PostComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

        labels ={
            'text' : 'your comment'
        }

        widgets = {
            'text': forms.Textarea(attrs={
                'style': 'height: 20px;width:500px'}),
        }




