from django import forms

from . import models

#REVENIR DESSUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = models.Photo
#         fields = ['image', 'caption']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ['headline', 'body']
