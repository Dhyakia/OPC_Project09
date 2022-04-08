from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authentication import views as authV
from review import views as reviV


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authV.login, name='login'),
    path('logout/', authV.logout, name='logout'),
    path('signup/', authV.signup, name='signup'),
    path('review/follows/', reviV.follows, name='follows'),
    path('review/flux/', reviV.flux, name='flux'),
    path('review/my_content/', reviV.myContent, name='my-content'),
    path('review/create_ticket/', reviV.createTicket, name='create-ticket'),
    path('review/create_review/', reviV.createReview, name='create-review'),
    path('review/create_critic/<int:id>/', reviV.createCritic, name="create-critic"),
    path('review/edit_ticket/<int:id>/', reviV.editTicket, name='edit-ticket'),
    path('review/edit_review/<int:id>/', reviV.editReview, name='edit-review'),
    path('review/delete_ticket/<int:id>/', reviV.deleteTicket, name='delete-ticket'),
    path('review/delete_review/<int:id>/', reviV.deleteReview, name='delete-review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
