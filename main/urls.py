
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from compositions.views import profile
from compositions import views

urlpatterns = [
    path('', views.index, name='home'),
    path('like/', views.like_song, name='like_song'),
    path('comment/', views.post_comment, name='post_comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contacts'),
    path('signup/', views.signup, name='signup'),  # добавлен путь для регистрации
    path('login/', auth_views.LoginView.as_view(), name='login'),  # добавлен путь для входа
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # добавлен путь для выхода
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/', include('django.contrib.auth.urls')),  # добавлено подключение URL-путей Django для авторизации
    path('accounts/profile/', profile, name='profile'),
]
