from django.urls import path, include


from . import views
from .views import Search
urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('login/', views.login_U, name="login_U"),
    path('logout/', views.logout_U, name="logout_U"),
    path('register/', views.reg_U, name="register"),
    path('update_user/', views.update_u_info, name="update_u_info"),
    path('update_p/', views.update_u_p, name="update_p"),
    path('product/<int:pk>', views.product, name="product"),
    path('category/<str:foo>', views.category, name="category"),
    path('category/C_menue/<str:foo>', views.C_menue, name="C_menue"),
    # path('search/<int:np>', views.search, name="search"),
    path('search/<int:np>', Search.as_view(), name="search"),

    path('update_item/', views.updateItem, name="update_item"),
    path('add_p/', views.add_p, name="add_p"),

    # path('cart/', include("cart.urls")),
     
    
    
 
]