from django.contrib import admin

# Register your models here.
from .models import Menu, Blog, Comment

admin.site.register(Menu)
admin.site.register(Blog)
admin.site.register(Comment)

