from django.urls import path

from DjangoWebSockets.mywebsite.views import lobby

urlpatterns = (
    path('', lobby),
)