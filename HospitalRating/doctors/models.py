
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from HospitalRating.patients.models import Patients
from HospitalRating.core.validators import validate_file_size_5mb

UserModel = get_user_model()


class Doctor(models.Model):
    DOCTOR_DESCRIPTION_MAX_LEN = 300
    DOCTOR_DESCRIPTION_MIN_LEN = 10

    photo = models.FileField(
        upload_to='images',
        validators=(
            validate_file_size_5mb,
        ),
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=DOCTOR_DESCRIPTION_MAX_LEN,
        validators=(MinLengthValidator(DOCTOR_DESCRIPTION_MIN_LEN),),
        blank=True,
        null=True,
    )

    tagged_patient = models.ManyToManyField(
        Patients,
        blank=True,
    )

    date_of_discharge = models.DateField(
        auto_now=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
