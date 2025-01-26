from django.contrib import admin
from apply.models import Apply
# Register your models here.
class ApplyAdmin(admin.ModelAdmin):
    list_display=('apply_fname','apply_lname','apply_email','apply_gender','apply_pincode','apply_phone','apply_position','apply_date','apply_address','apply_coverletter',)
admin.site.register(Apply,ApplyAdmin)
