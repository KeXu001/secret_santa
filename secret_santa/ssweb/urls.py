
from django.urls import path

from .views import join_game, review_login, review

urlpatterns = [
    path('join/<uuid:code>', join_game, name='join-game'),
    path('review/<uuid:code>', review_login, name='review-login'),
    path('review/participant/<int:participant_id>', review, name='review'),
]