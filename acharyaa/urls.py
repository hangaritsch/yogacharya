
from django.urls import path
from acharyaa import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('signup', views.signup, name="signup"),
    path('login', views.handlelogin, name="handlelogin"),
    path('logout', views.handleLogout, name='handleLogout'),
    path('contact', views.contact, name="contact"),
    path('join', views.enroll, name="join"),
    path('profile', views.profile, name="profile"),
    path('services',views.services, name="services"),
    path('gallery',views.gallery, name='gallery'),
    path('about',views.about, name='about'),
]

   