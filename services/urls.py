from django.urls import path
from . import views

urlpatterns = [
    path('handle/', views.handle, name='handle'),
    path('play/', views.play, name='play'),
    path('music/',views.music, name='music'),
    path('Social/',views.social, name='Social'),
    path('online/',views.online, name='online'),
    path('art/',views.art, name='art'),
    path('emdr/',views.emdr, name='emdr'),
    path('cbt/',views.cbt,name='cbt'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('explore/', views.explore, name='explore'),
    path('form/',views.form, name="form"),
    path('onlineform/',views.onlineform, name="onlineform")

]