from django import forms 
from . import models
from django.core.validators import ValidationError

class CreatePost(forms.ModelForm): 
    class Meta: 
        model = models.Post
        fields = ['title','body','slug','banner']
        widgets = {
            'body': forms.Textarea(attrs={'class': "form-control"})
        }
    def clean(self):
        banner = self.cleaned_data['banner']
        if banner == "fallback.png":
            raise ValidationError("No Image uploaded")