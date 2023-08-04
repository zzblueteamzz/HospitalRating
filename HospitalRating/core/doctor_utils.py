from HospitalRating.doctors.models import Doctor


def apply_likes_count(doctor):
    doctor.likes_count = doctor.photolike_set.count()
    return doctor


def apply_user_liked_doctor(doctor):
    # TODO: fix this for current user when authentication is available
    doctor.is_liked_by_user = doctor.likes_count > 0
    return doctor


def find_doctor_by_pk(pk):
    return Doctor.objects.filter(pk=pk).get()