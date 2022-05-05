from django.urls import path
from .import views
from .views import EmailAttachementView, RegisterUser

urlpatterns = [
    path('', views.home, name='index'),
    path('send/', EmailAttachementView.as_view(), name='emailattachment'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]