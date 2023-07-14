from django.contrib import admin
from .models import Post, Contacts

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number']
    search_fields = ['name', 'email', 'number']
    list_per_page = 6

admin.site.register(Post)


admin.site.register(Contacts)

