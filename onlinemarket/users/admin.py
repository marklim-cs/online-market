from django.contrib import admin
from .models import CustomUser, City

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'city')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(City, CityAdmin)
