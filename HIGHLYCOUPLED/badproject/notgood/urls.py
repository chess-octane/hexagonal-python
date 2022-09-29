from django.urls import path
from notgood.views import ApplicationView

urlpatterns = [
    path('app', ApplicationView.as_view()),
]
