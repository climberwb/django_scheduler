from django.contrib import admin
from .models import Schedule, Activity
# Register your models here.
class ActivityAdminInline(admin.TabularInline):
    model = Activity
    fk_name = "schedule"

class ScheduleAdmin(admin.ModelAdmin):
    inlines = (ActivityAdminInline, )
 
admin.site.register(Schedule, ScheduleAdmin)