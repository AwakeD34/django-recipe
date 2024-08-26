from django.urls import path
from calculator.views import omlet, pasta, buter, start

urlpatterns = [
    path('', start),
    path('omlet/', omlet),
    path('pasta/', pasta),
    path('buter/', buter),
]
