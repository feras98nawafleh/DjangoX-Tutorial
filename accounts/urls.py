from django.urls import path
from .views import AccountLogin

urlpatterns = [
  path('login/', AccountLogin.as_view(), name='login')
]