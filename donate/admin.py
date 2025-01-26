from django.contrib import admin
# Register your models here.
from donate.models import Donate
class DonateAdmin(admin.ModelAdmin):
    list_display=('donate_number','donate_holder','donate_expiry','donate_cvc',)
admin.site.register(Donate,DonateAdmin)
