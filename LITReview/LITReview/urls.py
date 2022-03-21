from django.contrib import admin
from django.urls import path

from authentication import views as authV
from review import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authV.login, name='login-page'),
]
