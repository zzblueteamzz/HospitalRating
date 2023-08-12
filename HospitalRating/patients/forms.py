from django import forms

from HospitalRating.core.form_mixins import DisabledFormMixin
from HospitalRating.patients.models import Patients


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models

class PatientBaseForm(forms.ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        #fields = ('name', 'date_of_birth', 'diagnosis', 'personal_photo')
        exclude = ('slug',)
        labels = {
            'name': 'Name of Patient',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
            'diagnosis': 'Diagnosis',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Patient name'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'diagnosis': forms.TextInput(
                attrs={
                    'placeholder': 'Patient diagnosis'
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            )
        }


class PatientCreateForm(PatientBaseForm):
    pass


class PatientEditForm(DisabledFormMixin, PatientBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class PatientDeleteForm(DisabledFormMixin, PatientBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'diagnosis', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
