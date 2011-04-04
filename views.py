# http://stackoverflow.com/questions/3402708/django-urls-straight-to-html-template/3402840#3402840
from django.views.generic.simple import direct_to_template
from django.http import Http404

def home(request, home):
    # Use some exception handling, just to be safe
    try:
        return direct_to_template(request, '/' % (request, base.html))
    except TemplateDoesNotExist:
        raise Http404