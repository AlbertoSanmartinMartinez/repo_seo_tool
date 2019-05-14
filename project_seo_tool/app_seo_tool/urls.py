
#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.urls import path
from django.contrib.auth import views as auth_views

from app_seo_tool import views as app_seo_views


urlpatterns = [

    # General urls
    path('', app_seo_views.home, name='home'),

    path('acceso/', app_seo_views.custom_login, name='custom_login'),
    path('desconectar/', auth_views.LogoutView.as_view(), name='logout'),
    path('activacion/<uidb64>/<token>/', app_seo_views.activation, name='activation'),
    path('password_reset/', app_seo_views.password_reset, name='password_reset'),
    path('password_reset_form/<uidb64>/<token>/', app_seo_views.password_reset_form, name='password_reset_form'),

    path('resultados/', app_seo_views.result_list, name='result_list'),
    #path('resultados/filtrar/', app_seo_views.result_filter, name='result_filter'),#

    path('busquedas/', app_seo_views.search_list, name='search_list'),
    #path('busquedas/crear/', app_seo_views.search_create, name='search_create'),
    #path('busquedas/filtrar/', app_seo_views.search_filter, name='search_filter'),
]
