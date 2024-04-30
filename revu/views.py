from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from . import forms, models


@login_required
def home(request):
    reviews = models.Review.objects.all()
    return render(request, 'revu/home.html', context={'reviews': reviews})


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

@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'revu/view_review.html', {'review': review})
