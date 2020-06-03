from django.urls import path

from .views import CreditDetailView, InstitutionDetailView, InstitutionIndexView

app_name = 'Education'
urlpatterns = [
    path('', InstitutionIndexView.as_view(), name='index'),
    path('class/<int:pk>/', CreditDetailView.as_view(), name='credit-detail'),
    path('school/<int:pk>/', InstitutionDetailView.as_view(), name='institution-detail'),
]
