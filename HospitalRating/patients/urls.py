from django.urls import path, include

from HospitalRating.patients.views import add_patient, show_patient_details, edit_patient, delete_patient

# pets/urls
# http://127.0.0.1:8000/pets/goto/pet/Buddy/ + edit/delete

urlpatterns = (
    path('add/', add_patient, name='add_patient'),
    path('<str:username>/patient/<int:pk>/', include(
        [
            path('', show_patient_details, name='show pet details'),
            path('edit/', edit_patient, name='edit_patient'),
            path('delete/', delete_patient, name='delete_patient'),
        ]
    )),
)
