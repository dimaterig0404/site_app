from django.contrib import admin

#python manage.py createsuperuser

from .models import USER,II,SEANS,DATA_ALL_SEANSES

admin.site.register(USER)
admin.site.register(II)
admin.site.register(SEANS)
admin.site.register(DATA_ALL_SEANSES)