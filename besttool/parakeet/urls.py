from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = "parakeet"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('sha-upload/', views.sha_upload_page, name='sha_uploader')
    # path('admin/', admin.site.urls),
]