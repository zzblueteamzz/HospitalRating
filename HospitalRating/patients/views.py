from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from HospitalRating.common.forms import CommentForm
from HospitalRating.core.find_patient import get_patient_by_name_and_username
from HospitalRating.core.is_owner import is_owner
from HospitalRating.patients.forms import PatientEditForm, PatientCreateForm, PatientDeleteForm


@login_required
# pets/views.py
def add_patient(request):
    if request.method == "GET":
        form = PatientCreateForm()
    else:
        form = PatientCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('profile details', pk=request.user.pk)

    context = {
        'form': form,

    }

    return render(
        request,
        'patients/patient-add-page.html',
        context,
    )


def show_patient_details(request, username, patient_slug):
    patient = get_patient_by_name_and_username(patient_slug, username)
    all_photos = patient.photo_set.all()
    comment_form = CommentForm()

    context = {
        'patient': patient,
        'all_photos': all_photos,
        'comment_form': comment_form,
        'username': username,
        'patient_slug': patient_slug,
        'is_owner': patient.user == request.user,

    }

    return render(
        request,
        'patients/patient-details-page.html',
        context,
    )


def edit_patient(request, username, patient_slug):
    patient = get_patient_by_name_and_username(patient_slug, username)

    if not is_owner(request, patient):
        return redirect('show_patient_details', username=username, patient_slug=patient_slug)

    if request.method == 'GET':
        form = PatientEditForm(instance=patient)
    else:
        form = PatientEditForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('show_patient_details', username=username, patient_slug=patient_slug)

    context = {
        'form': form,
        'patient': patient,
        'username': username,
        'patient_slug': patient_slug,
    }
    return render(
        request,
        'patients/patient-edit-page.html',
        context,
    )


def delete_patient(request, username, patient_slug):
    patient = get_patient_by_name_and_username(patient_slug, username)
    profile = patient.user

    if request.method == 'GET':
        form = PatientDeleteForm(instance=patient)
    else:
        form = PatientDeleteForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=profile.pk)

    context = {
        'form': form,
        'patient': patient,
        'patient_slug': patient_slug,
        'username': username,
    }

    return render(
        request,
        'patients/patient-delete-page.html',
        context,
    )



