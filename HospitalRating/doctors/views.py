from django.core.files.uploadedfile import UploadedFile

from django.shortcuts import render, redirect
from django.urls import reverse

from HospitalRating.common.forms import CommentForm
from HospitalRating.core.doctor_utils import find_doctor_by_pk
from HospitalRating.doctors.forms import DoctorCreateForm, DoctorEditForm, DoctorDeleteForm


def add_doctor(request):
    if request.method == 'GET':
        form = DoctorCreateForm()
    else:
        form = DoctorCreateForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file=UploadedFile(photo=request.FILES['photo'])
            uploaded_file.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(
        request,
        'doctors/doctor-add-page.html',
        context,
    )


def show_doctor_details(request, pk):
    doctor = find_doctor_by_pk(pk)
    likes = doctor.like_set.all()
    comments = doctor.comment_set.all()
    comment_form = CommentForm()

    context = {
        'doctor': doctor,
        'likes': likes,
        'comments': comments,
        'comment_form': comment_form,
        'is_owner': request.user == doctor.user,

    }

    return render(
        request,
        'doctors/doctor-details-page.html',
        context,
    )


def get_post_photo_form(request, form, success_url, template_path, pk=None):
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(success_url)

    context = {
        'form': form,
        'pk': pk,
    }

    return render(request, template_path, context)


def edit_doctor(request, pk):
    doctor = find_doctor_by_pk(pk)
    return get_post_photo_form(
        request,
        DoctorEditForm(request.POST or None, instance=doctor),
        success_url=reverse('index'),
        template_path='doctors/doctor-edit-page.html',
        pk=pk,
    )


def delete_doctor(request, pk):
    doctor = find_doctor_by_pk(pk)

    return get_post_photo_form(
        request,
        DoctorDeleteForm(request.POST or None, instance=doctor),
        success_url=reverse('index'),
        template_path='doctors/doctor-edit-page.html',
        pk=pk,
    )

