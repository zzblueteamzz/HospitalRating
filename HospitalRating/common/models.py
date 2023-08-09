from django.contrib.auth import get_user_model
from django.db import models
from HospitalRating.doctors.models import Doctor

UserModel = get_user_model()


class Comment(models.Model):
    comment_text = models.TextField(max_length=300, blank=False, null=False)
    # optional
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE, )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ('-date_time_of_publication',)


class Like(models.Model):
    to_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)


