from django.urls import path
from . import views

urlpatterns = [
    path('integrated/', views.integrated_view, name='integrated'), # New integrated view
]