from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.vlistview, name='home-page'),
    path('register/', views.register, name='register-page'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login-page'),
    path('newnote/', views.newnote, name='new-note'),
    path('mynote/', views.noteView, name='my_note'),
    path('voucherlst/', views.vlistview, name='vlist'),
    path('voucher/', views.voucherView, name='voucher'),
    path('createvch/', views.createVoucher, name='create-voucher'),
    path('delete/', views.deleteV, name='delete'),
    path('notices/', views.home, name='note-home'),
    
    
]