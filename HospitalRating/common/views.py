from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
            all_doctors = all_doctors.filter(tagged_patient__name__icontains=search_form.cleaned_data['pet_name'])

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

@login_required
def like_functionality(request, photo_id):
    photo = Patients.objects.get(pk=photo_id)

    kwargs = {
        'to_photo': photo,
        'user': request.user
    }

    like_object = Like.objects \
        .filter(**kwargs) \
        .first()

    if like_object:
        like_object.delete()
    else:
        new_like_object = Like(**kwargs)
        new_like_object.save()

    # http://127.0.0.1:8000/
    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


@login_required
def share_functionality(request, photo_id):
    # copy(request.META['HTTP_HOST'] + resolve_url('photo details', photo_id))

    return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


@login_required
def comment_functionality(request, photo_id):
    photo = Patients.objects.get(pk=photo_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            print('form is valid')

            new_comment_instance = form.save(commit=False)
            new_comment_instance.to_photo = photo
            new_comment_instance.save()

        return redirect(request.META['HTTP_REFERER'] + f"#{photo_id}")


