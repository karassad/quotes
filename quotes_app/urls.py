from django.urls import path
from .views import random_quote, like_quote, dislike_quote

urlpatterns = [
    path('', random_quote, name='random_quote'),
    path('like/<int:quote_id>/', like_quote, name='like_quote'),
    path('dislike/<int:quote_id>/', dislike_quote, name='dislike_quote'),
    ]

