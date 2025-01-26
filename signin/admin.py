from django.contrib import admin
# Register your models here.
from signin.models import Signin
class SigninAdmin(admin.ModelAdmin):
    list_display=('signin_name','signin_email','signin_password',)
admin.site.register(Signin,SigninAdmin)
