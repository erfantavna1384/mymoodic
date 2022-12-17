from django.urls import  path
from blog_app import views
from blog_app.models import Article
app_name= 'post_detail'
urlpatterns = [
    path("",views.home_app,name="home"),
    path('detail/<int:pk>',views.post_detail,name="post_detail"),

]