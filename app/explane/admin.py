from django.contrib import admin

from .models import Explane

class ExplaneAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "time_from", "time_to", "user")

admin.site.register(Explane, ExplaneAdmin)
