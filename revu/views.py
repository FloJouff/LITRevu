from itertools import chain
from django.db.models import CharField, Value, Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from authentication.models import User

from . import forms, models
from .models import UserFollows, BlockedUser


@login_required
def home(request):
    """Feed view

    """
    user = request.user
    blocked_users = BlockedUser.objects.filter(user=user).values_list(
        'blocked_user', flat=True)
    following_users = User.objects.filter(
        id__in=UserFollows.objects.filter(user=user).values('followed_user'))
    tickets = models.Ticket.objects.filter(
        Q(user__in=following_users) |
        Q(user=user) &
        ~Q(user__in=blocked_users)).annotate(content_type=Value('TICKET',
                                                                CharField()))
    reviews = models.Review.objects.filter(
        Q(user__in=following_users) |
        Q(user=user) |
        Q(ticket__in=tickets) &
        ~Q(user__in=blocked_users)).annotate(content_type=Value('REVIEW',
                                                                CharField()))
    posts = sorted(chain(reviews, tickets),
                   key=lambda post: post.time_created,
                   reverse=True)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
        }
    return render(request, 'revu/home.html', context=context)


def contact(request):
    """Contact view

    """
    return render(request, 'revu/contact.html')


def no_permission(request):
    """View if user is not allowed to edit or delete a post

    """
    return render(request, 'revu/no_permission.html')


@login_required
def user_posts(request):
    """User's posts view
    """
    reviews = models.Review.objects.filter(
        user=request.user).annotate(content_type=Value('REVIEW', CharField()))
    tickets = models.Ticket.objects.filter(
        user=request.user).annotate(content_type=Value('TICKET', CharField()))
    posts = sorted(chain(reviews, tickets),
                   key=lambda post: post.time_created,
                   reverse=True)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
        }
    return render(request, 'revu/posts.html', context=context)


@login_required
def review_response(request, ticket_id):
    """Create a review for an existing ticket

    Args:
        ticket_id (int): ticket's id


    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()

    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            ticket.review_provided = True
            ticket.save()
            review.save()
            return redirect('home')
    return render(request, 'revu/review_response.html',
                  context={'review_form': review_form, 'ticket': ticket})


@login_required
def create_new_review(request):
    """Create a ticket and a review in the same time

    """
    ticket_form = forms.TicketForm(prefix='ticket')
    review_form = forms.ReviewForm(prefix='review')

    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES,
                                       prefix='ticket')
        review_form = forms.ReviewForm(request.POST, prefix='review')

        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.review_provided = True
            ticket.save()

            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect('home')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'revu/create_new_review.html', context=context)


@login_required
def view_review(request, review_id):
    """Allow to select a review

    Args:

        review_id (int): review's id
    """
    review = get_object_or_404(models.Review, id=review_id)
    return render(request, 'revu/view_review.html', {'review': review})


@login_required
def edit_review(request, review_id):
    """Edit a review

    Args:

        review_id (int): review's id
    """
    review = get_object_or_404(models.Review, id=review_id)
    if review.user != request.user:
        return redirect('no_permission')
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
def delete_review(request, review_id):
    """Delete a review

    Args:

        review_id (int): review's id
    """
    review = get_object_or_404(models.Review, id=review_id)
    if request.user == review.user:
        review.delete()
        # review.ticket.review_provided = False
        messages.success(request, "La critique a été supprimée avec succès.")
    else:
        messages.error(request,
                       "Vous n'êtes pas autorisé à supprimer cette critique.")

    return redirect('user_posts')


@login_required
def create_ticket(request):
    """Create a new ticket

    """
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
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
    """Allow to view a ticket

    Args:

        ticket_id (int): ticket's id
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    return render(request, 'revu/view_ticket.html', {'ticket': ticket})


@login_required
def edit_ticket(request, ticket_id):
    """Edit a ticket

    Args:
        ticket_id (int): ticket's id

    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if ticket.user != request.user:
        return redirect('no_permission')
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST,
                                         request.FILES, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'revu/edit_ticket.html', context=context)


@login_required
def delete_ticket(request, ticket_id):
    """Delete a ticket

    Args:
        ticket_id (int): ticket's id
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    if request.user == ticket.user:
        ticket.delete()
        messages.success(request, "Le ticket a été supprimé avec succès.")
    else:
        messages.error(request,
                       "Vous n'êtes pas autorisé à supprimer ce ticket.")

    return redirect('user_posts')


def follow_users(request):
    """Follow new user, see who follows who


    """
    form = forms.FollowUsersForm(request.POST or None)
    followings = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            user_to_follow = User.objects.get(username=username)
            UserFollows.objects.get_or_create(user=request.user,
                                              followed_user=user_to_follow)
            return redirect('follow')

    context = {
        'form': form,
        'followings': followings,
        'followers': followers,
    }
    return render(request, 'revu/follow_view.html', context=context)


def unfollow_user(request, user_id):
    """unfollow a user

    Args:
        user_id (int): user's id

    """
    user = request.user
    followed_user = User.objects.get(id=user_id)
    try:
        follow = UserFollows.objects.get(user=user,
                                         followed_user=followed_user)
        follow.delete()
    except UserFollows.DoesNotExist:
        pass
    return redirect('follow')


def block_user(request):
    """Block a user, see who user is blocking


    """
    form = forms.FollowUsersForm(request.POST or None)
    user = request.user
    blocked_user = BlockedUser.objects.filter(user=request.user)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            user_to_block = User.objects.get(username=username)
            BlockedUser.objects.get_or_create(user=request.user,
                                              blocked_user=user_to_block)
            messages.success(request, "L'utilisateur a été bloqué avec succès")
            UserFollows.objects.filter(user=user,
                                       followed_user=user_to_block).delete()
            UserFollows.objects.filter(user=user_to_block,
                                       followed_user=user).delete()
            return redirect('block_view')
    context = {
        'block_form': form,
        'user': user,
        'blocked_users': blocked_user,
    }
    return render(request, 'revu/block_view.html', context=context)


def unblock_user(request, user_id):
    """unblock a user

    Args:
        user_id (int): user's id

    """
    user = request.user
    blocked_user = User.objects.filter(id=user_id).first()

    if blocked_user:
        BlockedUser.objects.filter(user=user,
                                   blocked_user=blocked_user).delete()
        messages.success(request, "L'utilisateur a été débloqué avec succès.")
        if not UserFollows.objects.filter(user=user,
                                          followed_user=blocked_user).exists():
            UserFollows.objects.create(user=user, followed_user=blocked_user)
        if not UserFollows.objects.filter(user=blocked_user,
                                          followed_user=user).exists():
            UserFollows.objects.create(user=blocked_user, followed_user=user)

    return redirect('block_view')
