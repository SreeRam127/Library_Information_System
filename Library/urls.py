from Library import views
from django.contrib import admin
from django.urls import path,include
from Library import views
urlpatterns = [
    path('', views.Library, name='Library'),
    path('add_user/',views.add_user),
    path('add_user/create_user/', views.create_user),
    path('all_user/', views.all_user),
    path('home/', views.home),
    path('books/', views.books, name='books'),
    path('view_book/', views.view_book, name='view_book'),
    path('send_book/', views.send_book, name='send_book'),
    path('login/', views.userLogin, name='userLogin'),
    path('logoutUser/', views.logoutUser, name='logoutUser'),
    path('user/edit_user/',views.edit_user),
    path('user/edit_user/update_user/',views.update_user),
    path('user/profile_view/',views.profile_view),
    # path('users/profile_view/add_book/',views.add_book_to_user),
    # path('users/profile_view/delete_book/',views.delete_book),
    ]