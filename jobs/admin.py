from django.contrib import admin
# Register your models here.
from jobs.models import Job
class JobsAdmin(admin.ModelAdmin):
    list_display=('job_title','job_location','job_salary','job_type','job_desc',)
admin.site.register(Job,JobsAdmin)
