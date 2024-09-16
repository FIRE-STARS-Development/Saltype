from django.urls import path
from .views import AddScoreAndRankView

urlpatterns = [
    path('insert-result/', AddScoreAndRankView.as_view(), name='insert-result'),
]
