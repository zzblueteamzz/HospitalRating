from HospitalRating.patients.models import Patients


def get_patient_by_name_and_username(patient_slug, username):
    return Patients.objects.filter(
        slug=patient_slug,
        user__username=username).get()