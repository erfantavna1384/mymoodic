from django.urls import  path
from account_app import views
from blog_app.models import Article
app_name= 'account_app'
urlpatterns = [
    path("user_register/", views.register, name="register"),
    path("user_login/", views.user_login, name="login"),
    path("user_logout/", views.user_logout, name="logout"),
]