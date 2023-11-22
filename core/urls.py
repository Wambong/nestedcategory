from django.urls import path
from django.contrib.auth import views
from core.views import frontpage, contact, about

from store.views import  search

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),

]
