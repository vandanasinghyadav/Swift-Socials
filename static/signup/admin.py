from django.contrib import admin
# Register your models here.
from signup.models import Signup
class SignupAdmin(admin.ModelAdmin):
    list_display=('signup_name','signup_email','signup_password',)
admin.site.register(Signup,SignupAdmin)
