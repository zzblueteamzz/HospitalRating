from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
UserModel = get_user_model()


class Patients(models.Model):
    NAME_MAX_LEN = 30
    personal_photo = models.URLField(
        blank=False,
        null=False,
    )
    name = models.CharField(
        max_length=NAME_MAX_LEN,

    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    diagnosis = models.CharField(
        blank=False,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,

    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

