from django.contrib import admin
from . models import Report
# Register your models here.
class ReportModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pdf', 'discription','cover')

admin.site.register(Report, ReportModelAdmin)