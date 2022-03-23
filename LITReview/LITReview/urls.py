from django.contrib import admin
from django.urls import path

from authentication import views as authV
from review import views as reviV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authV.login, name='login'),
    path('signup/', authV.signup, name='signup'),
    path('review/flux/', reviV.flux, name='flux'),
    path('review/follows/', reviV.follows, name='follows'),
    path('review/create_ticket/', reviV.createTicket, name='create-ticket'),
    path('review/new_review/', reviV.createReview, name='new-review'),
    path('review/my_content/', reviV.myContent, name='my-content'),

]
