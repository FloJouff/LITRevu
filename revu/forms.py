from django import forms

from . import models

#REVENIR DESSUS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = models.Photo
#         fields = ['image', 'caption']


class ReviewForm(forms.ModelForm):
    CHOICES = [('0', '- 0'), ('1', '- 1'), ('2', '- 2'),
                   ('3', '- 3'), ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    class Meta:
        
        model = models.Review
        fields = ('headline', 'rating', 'body')
        labels = {'headline': 'Titre', 'rating': 'Note', 'body': 'Commentaire'}

        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control', 'label': 'Titre'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
