from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from compositions.views import *
from compositions import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page URL
    path('like/', views.like_song, name='like_song'),
    path('comment/', views.post_comment, name='post_comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contacts'),
    path('signup/', views.signup, name='signup'),  # добавлен путь для регистрации
    path('accounts/login/', login_view, name='login'),  # добавлен путь для входа
    # path('login/', auth_views.LoginView.as_view(), name='login'),  # добавлен путь для входа
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),  # добавлено подключение URL-путей Django для авторизации
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/password_change/', change_password, name='password_change',),
    path('songs/', views.songs_home, name='songs_home'),
    path('create/', views.create, name='create'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
]
