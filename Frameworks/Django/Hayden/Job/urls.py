from django.urls import path

from .views import CareerDetailView, CareerIndexView

app_name = 'Job'
urlpatterns = [
    path('<int:pk>/', CareerDetailView.as_view(), name='career-detail'),
    path('jobs', CareerIndexView.as_view()),
]
