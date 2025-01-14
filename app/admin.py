from django.contrib import admin
from .models import BootcampRegistration

# Register your models here.

@admin.register(BootcampRegistration)
class BootcampRegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'role', 'registered_at')
    search_fields = ('full_name', 'email', 'role')
