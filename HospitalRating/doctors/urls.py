from django.urls import path, include

from HospitalRating.doctors.views import add_doctor, show_doctor_details, edit_doctor, delete_doctor

# photos/urls

urlpatterns = (
    path('', include(
        [
            path('add/', add_doctor, name='add_doctor '),
            path('<int:pk>/', show_doctor_details, name='show_doctor_details'),
            path('edit/<int:pk>/', edit_doctor, name='edit_doctor'),
            path('delete/<int:pk>/', delete_doctor, name='delete_doctor'),
        ]
    )),

)