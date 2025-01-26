from django.contrib import admin
# Register your models here.
from login.models import Login
class LoginAdmin(admin.ModelAdmin):
    list_display=('login_email','login_password',)
admin.site.register(Login,LoginAdmin)
