import pyperclip
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from HospitalRating.patients.models import Patients
from .forms import CommentForm, SearchForm
from .models import Like
from ..doctors.models import Doctor


def index(request):
    all_doctors = Doctor.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm()

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            all_doctors = all_doctors.filter(tagged_patient__name__icontains=search_form.cleaned_data['patient_name'])

    context = {
        'all_doctors': all_doctors,
        'comment_form': comment_form,
        'search_form': search_form,
    }

    return render(
        request,
        'common/home-page.html',
        context,
    )


def like_functionality(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    liked_object = Like.objects.filter(to_doctor=doctor_id, user_id=request.user.pk)

    if liked_object:
        liked_object.delete()
    else:
        Like.objects.create(
            to_doctor=doctor,
            user_id=request.user.pk,
        )

    return redirect(request.META['HTTP_REFERER'] + f'#{doctor_id}')

def get_photo_url(request, doctor_id):
    return request.META['HTTP_REFERER'] + f'#photo-{doctor_id}'


def share_functionality(request, doctor_id):
    photo_details_url = reverse('show_doctor_details', kwargs={
        'pk': doctor_id
    })
    pyperclip.copy(photo_details_url)
    return redirect(get_photo_url(request, doctor_id))


@login_required
def comment_functionality(request, doctor_id):
    if request.method == 'POST':
        doctor = Doctor.objects.filter(pk=doctor_id).get()

        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_doctors = doctor
            comment.user = request.user
            comment.save()

        return redirect(
            request.META['HTTP_REFERER'] + f'#{doctor_id}'
        )



def redirect_to_index(request):
    return redirect('index')