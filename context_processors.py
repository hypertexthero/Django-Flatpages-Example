# http://stackoverflow.com/questions/4256145/django-template-tag-to-display-django-version/6423192#6423192
import django
def django_version(request):
    return { 'django_version': django.VERSION }