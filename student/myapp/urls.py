from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home', views.fnhome,name='home'),
    path('ad-login', views.fnad_login,name='ad-login'),
    path('ad-home', views.fnad_home,name='ad-home'),
    path('user-login', views.fnuser_login,name='user-login'),
    path('admin-logout',views.fnadmin_logout,name='admin-logout'),
    path('user-logout',views.fnuser_logout,name='user-logout'),
    path('user-reg', views.fnuser_reg,name='user-reg'),
    path('status-stud', views.fnstatus_stud,name='status-stud'),
    path('active-stud', views.fnactive_stud,name='active-stud'),
    path('inactive-stud', views.fninactive_stud,name='inactive-stud'),
    path('user-home', views.fnuser_home,name='user-home'),
    path('view-profile', views.fnview_profile,name='view-profile'),
    path('update-profile', views.fnupdate_profile,name='update-profile'),
    path('user-registration', views.fnuser_registration,name='user-registration'),
    
    
]