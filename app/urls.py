from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("add_recipe/",add_recipe,name='addrecipe'),
    path("",home,name='home'),
    path("delete/<int:id>",delete,name='delete'),
    path("update/",update,name='update'),
    path("update/<int:id>",update,name='update'),
    path("signup/",user_signup,name='signup'),
    path("login/",user_login,name='login'),
    path("logout/",user_logout,name='logout'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()
