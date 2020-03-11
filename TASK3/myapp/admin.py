from django.contrib import admin

# Register your models here.
from .models import Snippet

#register the snippet form for admin panel
admin.site.register(Snippet)
