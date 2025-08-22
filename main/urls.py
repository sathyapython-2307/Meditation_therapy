from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('therapy/', views.therapy_view, name='therapy'),
    path('about/', views.about_view, name='about'),
    path('meditation/', views.meditation_view, name='meditation'),
    path('contact/', views.contact_view, name='contact'),
    path('approach-form/', views.approach_form_view, name='approach_form'),
    path('approach-success/', views.approach_success_view, name='approach_success'),
    path('payment-details/', views.payment_details_view, name='payment_details'),
    path('payment-success/', views.payment_success_view, name='payment_success'),
]
