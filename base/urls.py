from django.urls import path
from . import views

app_name = 'base'
urlpatterns = [
    path('', views.base, name='base'),
    path('position', views.position, name='position'),
    path('position/<slug:oti>/<slug:zoomie>', views.zoom, name='zoom'),
    path('quotes/', views.quotes, name='quotes'),
    path('new-shipment/', views.new_shipment, name='new-shipment'),
    path('load-countries', views.load_countries, name='counts'),
    path('billing', views.billing, name='billing'),
    path('login', views.login_request, name='login'),
    path('sign-up', views.register, name='sign-up'),
    path('logout', views.logout_request, name='logout'),
    path('tracking', views.tracking, name='tracking'),
    path('profile', views.profile, name='profile'),
    path('pfp', views.pfp, name='pfp'),
    path('mailer/', views.mailer, name='mailer'),
    path('create-new', views.create_new, name='create_new'),
]
