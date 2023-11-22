
from django.urls import path

from django.contrib.auth import views

from userprofile.views import signup, myaccount



urlpatterns = [

    path('myaccount/', myaccount, name='myaccount'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

]
