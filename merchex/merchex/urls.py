"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('', views.homePage, name='home-page'),
    path('admin/', admin.site.urls),

    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/<int:band_id>/change', views.band_update, name='band-update'),
    path('bands/<int:band_id>/delete', views.band_remove, name='band-remove'),
    path('bands/add/', views.band_create, name='band-create'),

    path('listings/', views.annonces_list, name='liste_annnoces'),
    path('listings_detail/<int:annonce_id>/', views.annonce_detail, name='annonce-details'),
    path('listings_detail/<int:annonce_id>/change', views.annonce_update, name='annonce-update'),
    path('listings_detail/<int:annonce_id>/delete', views.annonce_remove, name='annonce-delete'),
    path('listings/add/', views.annonces_create, name='listing-create'),

    path('about/', views.about, name='about'),
    path('contact-us/', views.contact, name='contact'),
    path('contact-us/done/', views.email_sent, name='email-sent'),
]
