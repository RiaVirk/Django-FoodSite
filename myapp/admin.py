from django.contrib import admin
from myapp.models import Contact

admin.site.site_header = "Food Zone | Admin"
admin.site.site_title = "Food Zone | Admin"
admin.site.index_title = "Food Zone | Admin"


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email',
                    'subject', 'added_on', 'is_approved']


admin.site.register(Contact, ContactAdmin)
