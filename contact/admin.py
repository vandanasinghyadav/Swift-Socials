from django.contrib import admin
# Register your models here.
from contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=('contact_name','contact_email','contact_phone','contact_messege',)
admin.site.register(Contact,ContactAdmin)
