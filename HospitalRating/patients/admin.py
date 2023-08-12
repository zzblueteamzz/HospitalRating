from django.contrib import admin

from django.contrib import admin

from HospitalRating.patients.models import Patients




@admin.register(Patients)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
#
