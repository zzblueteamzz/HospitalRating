from django.contrib import admin


from HospitalRating.doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_discharge', 'description',)

    @staticmethod
    def get_tagged_patient(obj):
        return ', '.join([doctor.first_name for doctor in obj.tagged_patient.all()])
