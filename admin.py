# TODO: http://stackoverflow.com/questions/1021487/add-functionality-to-django-flatpages-without-changing-the-original-django-app

# from django.contrib import admin
# from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# 
# class FlatPageAdmin(admin.ModelAdmin):
#     content = models.TextField(_('content'), blank=True, help_text=_("<a href="http://daringfireball.net/projects/markdown/syntax" onclick="window.open(this.href, this.target); return false;">Markdown</a> syntax."))
#     pass
# admin.site.register(FlatPage, FlatPageAdmin)