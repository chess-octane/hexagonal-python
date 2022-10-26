from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from notgood.views import ApplicationView

urlpatterns = [
    path('application', csrf_exempt(ApplicationView.as_view())),
]
