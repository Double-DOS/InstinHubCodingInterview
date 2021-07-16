from django.urls import path
from .views import dash_board

urlpatterns = [
    path('1', dash_board)
]
