from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('home/',views.home,name='home'),
    path('book/',views.book,name='book'),
    path('details/<str:pk>/',views.details,name='details'),
    path('checkout/',views.checkout,name='checkout'),
    
    path('add_room/',views.add_room,name='add_room'),
    path('update_room/<str:pk>/',views.update_room,name='update_room'),
    path('delete_room/<str:pk>/',views.delete_room,name='delete_room'),
    path('delete_message/<str:pk>/',views.delete_message,name='delete_message'),
    
]
