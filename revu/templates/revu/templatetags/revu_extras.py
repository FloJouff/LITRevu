from django import template

register = template.Library()


@register.simple_tag(takes_contect=True)
def get_poster_display(context, user):
    if user == context['user']:
        return 'Vous'
    return user.username
