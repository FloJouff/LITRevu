from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from . import forms


@login_required
def home(request):
    return render(request, 'revu/home.html')


def contact(request):
    return render(request, 'revu/contact.html')

@login_required
def review_upload(request):
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
    context = {
        'review_form': review_form
    }
    return render(request, 'revu/create_review.html', context=context)