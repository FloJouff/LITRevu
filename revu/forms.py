from django import forms
from django.contrib.auth import get_user_model

from . import models


User = get_user_model()


class ReviewForm(forms.ModelForm):
    """Review form

    Args:
        forms : django form model
    """
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True,
                                     required=False)
    CHOICES = [('0', '- 0'), ('1', '- 1'), ('2', '- 2'), ('3', '- 3'),
               ('4', '- 4'), ('5', '- 5')]
    rating = forms.ChoiceField(choices=CHOICES,
                               label='Note',
                               widget=forms.RadioSelect(attrs={
                                   'class': 'd-flex m-2 p-2'}))

    class Meta:

        model = models.Review
        fields = ('headline', 'rating', 'body')
        labels = {'headline': 'Titre', 'rating': 'Note', 'body': 'Commentaire'}

        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control',
                                               'label': 'Titre'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'label': 'Commentaire'}),
        }


class DeleteReviewForm(forms.Form):
    """Delete Review Form

    """
    delete_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class TicketForm(forms.ModelForm):
    """Ticket form

    Args:
        forms : django form model
    """
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True,
                                     required=False)

    class Meta:
        model = models.Ticket
        fields = ('headline', 'body', 'image')
        labels = {'headline': 'Titre', 'body': 'Description', 'image': 'image'}

        widgets = {
            'headline': forms.TextInput(attrs={'class': 'form-control',
                                               'label': 'Titre'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 
                                          'label': 'Description'}),
        }


class DeleteTicketForm(forms.Form):
    """Delete ticket form

    """
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.Form):
    """Follow and block user forms

    Args:
        forms : django form model

    """
    username = forms.CharField(max_length=64, label='Nom d\'utilisateur')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Cet Utilisateur n\'existe pas.')
        return username

    class Meta:
        model = User
        fields = ['follow']
