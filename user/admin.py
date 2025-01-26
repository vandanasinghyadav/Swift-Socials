from django.contrib import admin
# Register your models here.
from user.models import User
class UserAdmin(admin.ModelAdmin):
    list_display=('user_email','user_password',)
admin.site.register(User,UserAdmin)
