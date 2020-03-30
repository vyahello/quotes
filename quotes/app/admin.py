"""Module represents API admin management."""
from django.contrib import admin
from .models import Quote

admin.site.register(Quote)
