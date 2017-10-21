from django.contrib import admin
from users.models import CholitoUser
# Register your models here.

@admin.register(CholitoUser)
class CholitoUserAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user", "user__username")
