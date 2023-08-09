from django.urls import path
from .views import index, like_functionality, share_functionality, comment_functionality, redirect_to_index

urlpatterns = [
    path('', index, name="index"),
    path('like/<int:doctor_id>', like_functionality, name="like"),
    path('share/<int:doctor_id>', share_functionality, name="share"),
    path('comment/<int:doctor_id>', comment_functionality, name="comment"),
    path('redirect_to_index/', redirect_to_index, name='redirect_to_index'),
]