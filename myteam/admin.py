from django.contrib import admin
from myteam.models import Team
# Register your models here.
class teamAdmin(admin.ModelAdmin):
    list_display=('team_title','team_name','team_salary','team_pic',)
admin.site.register(Team,teamAdmin)
