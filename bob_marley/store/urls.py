from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('login/', views.login_U, name="login_U"),
    path('logout/', views.logout_U, name="logout_U"),
    path('register/', views.reg_U, name="register"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:foo>', views.category, name="category"),

    
 
]
