from django import forms

from HospitalRating.common.models import Like, Comment
from HospitalRating.core.form_mixins import DisabledFormMixin
from HospitalRating.doctors.models import Doctor


class DoctorBaseForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorCreateForm(DoctorBaseForm):
    pass


class DoctorEditForm(forms.ModelForm):
    class Meta:
        model = Doctor
        exclude = ['photo']


class DoctorDeleteForm(DisabledFormMixin, DoctorBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_pets.clear()  # many-to-many

            Doctor.objects.all().first().tagged_pets.clear()
            Like.objects.filter(to_doctors_id=self.instance.id).delete()  # one-to-many
            Comment.objects.filter(to_doctors_id=self.instance.id).delete()  # one-to-many

            self.instance.delete()

        return self.instance