from django.contrib import admin
from .models import Books, Authors


admin.site.register(Books)
# Books registered to Admin Panel
admin.site.register(Authors)
