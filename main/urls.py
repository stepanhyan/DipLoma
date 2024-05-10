from django.urls import  include
from django.urls import path
from compositions.views import *
from compositions import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('songs/', views.songs_home, name='songs_home'),
    path('create/', views.create, name='create'),
    path('like/', views.like_song, name='like_song'),
    path('comment/', views.post_comment, name='post_comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contacts'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/password_change/', change_password, name='password_change',),
]
