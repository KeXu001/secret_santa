
from django.urls import path

from .views import join_game, review_login, review, update

urlpatterns = [
    path('join/<uuid:code>', join_game, name='join-game'),
    path('review/<uuid:code>', review_login, name='review-login'),
    path('review/participant/<int:participant_id>', review, name='review'),
    path('update/participant/<int:participant_id>', update, name='update'),
]