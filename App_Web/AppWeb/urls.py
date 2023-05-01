from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from AppWeb.views import *


urlpatterns = [
    path('', home, name="home"),
    path('details/', details, name="details"),
    path('memeros/', memeros, name="memeros"),
    path('profile/', profile, name="profile"),
    path('SignIn/', register, name="Sign_in"),
    path('store/', store, name="store"),
    path('fail/', fail, name="fail"),
    path('requestLogIn/', ask_log, name="requestLogIn"),
    path('tetris/', tetris, name="tetris"),
    path('bobble/', bobble, name="bobble"),
    path('sokoban/', sokoban, name="sokoban"),
#--- url to log in
    path('login/', login_usuario, name="Login"),
#--- url to log out
    path('logout/', LogoutView.as_view(template_name="logout.html"), name="Logout"),
#--- Registro
    path('register/', register, name="Register"),
    path('reg-product/', reg_product, name="reg-product"),
    path('product/<int:product_id>/', detail_product, name='details'),
    path('list-products/', list_products, name='list_products'),
#--- wallpaper    
    path('wallpapers/', wallpapers, name="wallpapers"),
    path('up-wallpaper/', up_image, name="up-wallpaper"),
    path('search/', search_images, name="search_images"),
]