from django.contrib import admin
from django.urls import path

from authentication import views as authV
from review import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', authV.login, name='login'),
    path('auth/signup/', authV.signup, name='signup'),
]