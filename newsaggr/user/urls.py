from django.urls import path
from user import views
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy

app_name = 'users'
urlpatterns = [
    path('',views.index,name="index"),
    path('business/',views.business,name="business"),
    path('entertainment/',views.entertainment,name="entertainment"),
    path('science/',views.science,name="science"),
    path('health',views.health,name="health"),
    path('sports/',views.sports,name="sports"),
    path('technology/',views.technology,name="technology"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',views.loggout, name='logout'),
    path('signup/',views.signup,name="signup"),
    path('forgot/',views.forgetpass,name="forgot"),
    path('preferance/',views.preferance,name="preferance"),
#    path('userprofile/',views.userprofile,name="userprofile"),'''
]