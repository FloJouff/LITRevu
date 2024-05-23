from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
import authentication.views
import revu.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('home/', revu.views.home, name='home'),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('revu/review_response/<int:ticket_id>/',
         revu.views.review_response, name='review_response'),
    path('revu/create_new_review/',
         revu.views.create_new_review, name='create_new_review'),
    path('revu/<int:review_id>/',
         revu.views.view_review, name='view_review'),
    path('revu/<int:review_id>/edit/',
         revu.views.edit_review, name="edit_review"),
    path('revu/delete-review/<int:review_id>/',
         revu.views.delete_review, name='delete_review'),
    path('revu/create_ticket/',
         revu.views.create_ticket, name='create_ticket'),
    path('revu/ticket/<int:ticket_id>/',
         revu.views.view_ticket, name='view_ticket'),
    path('revu/ticket/<int:ticket_id>/edit/',
         revu.views.edit_ticket, name='edit_ticket'),
    path('revu/delete-ticket/<int:ticket_id>/',
         revu.views.delete_ticket, name='delete_ticket'),
    path('contact/', revu.views.contact, name='contact'),
    path('no_permission', revu.views.no_permission, name='no_permission'),
    path('revu/posts/', revu.views.user_posts, name='user_posts'),
    path('revu/follow/', revu.views.follow_users, name='follow'),
    path('revu/unfollow/<int:user_id>/', revu.views.unfollow_user,
         name='unfollow_user'),
    path('revu/block/', revu.views.block_user,
         name='block_view'),
    path('revu/unblock/<int:user_id>/', revu.views.unblock_user,
         name='unblock_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
