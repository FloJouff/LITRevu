from django import forms

from . import models


# class PhotoForm(forms.ModelForm):
#     class Meta:
#         model = models.Photo
#         fields = ['image', 'caption']


class ReviewForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
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


class DeleteReviewForm(forms.Form):
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ('headline', 'body', 'image')
        labels = {'headline': 'Titre', 'body': 'Description', 'image': 'image'}

        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'image': forms.TextInput(attrs={'class': 'form-control'}),
        }
