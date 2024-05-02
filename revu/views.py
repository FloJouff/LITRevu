from django.shortcuts import render, redirect
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
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('home')
    context = {
        'review_form': review_form
    }
    return render(request, 'revu/create_review.html', context=context)


@login_required
def view_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'revu/view_review.html', {'review': review})


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
            if 'delete_review' in request.POST:
                delete_form = forms.DeleteReviewForm(request.POST)
                if delete_form.is_valid():
                    review.delete()
                    return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'revu/edit_review.html', context=context)


@login_required
def create_ticket(request):
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form
    }
    return render(request, 'revu/create_ticket.html', context=context)


@login_required
def view_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'revu/view_ticket.html', {'ticket': ticket})
