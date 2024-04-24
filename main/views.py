# from django.contrib import messages
# from django.contrib.auth import login
# from django.contrib.auth import update_session_auth_hash, logout
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.forms import PasswordChangeForm
# from django.http import JsonResponse
# from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
#
# from compositions.forms import LikeForm
# from compositions.forms import SongsForm
# from main.models import Songs, UserProfile, Like, Comment
# from .forms import SignUpForm
#
#
# # from main.models import Like, Comment
#
#
# @require_POST
# def like_song(request):
#     print("like_song view is called.")
#     form = LikeForm(request.POST)
#
#     if form.is_valid():
#         song_id = form.cleaned_data['song_id']
#         song = Songs.objects.get(id=song_id)
#
#         if request.user.is_authenticated:
#             user_profile = UserProfile.objects.get(user=request.user)
#
#             if Like.objects.filter(user=user_profile, song=song).exists():
#                 Like.objects.filter(user=user_profile, song=song).delete()
#             else:
#                 Like.objects.create(user=user_profile, song=song)
#
#             return JsonResponse({'status': 'success', 'likes': song.likes_users.count()})
#         else:
#             return JsonResponse({'status': 'error', 'message': 'User not authenticated'})
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid form data'})
#
#
# @require_POST
# def post_comment(request):
#     song_id = request.POST.get('song_id')
#     print(song_id)
#     comment_text = request.POST.get('comment')
#
#     if song_id and comment_text:
#         song = Songs.objects.get(id=song_id)
#         comment = Comment.objects.create(user=request.user, song=song, text=comment_text)
#
#         return JsonResponse({'status': 'success', 'comments': song.comments_users.count()})
#     return JsonResponse({'status': 'error'})
#
#
# def artist_detail(request, artist_id):
#     artist = get_object_or_404(Songs, id=artist_id)
#     return render(request, 'compositions/artist_detail.html', {'artist': artist})
#
#
# def songs_home(request):
#     compositions = Songs.objects.all()
#     return render(request, 'compositions/songs.html', {'compositions': compositions})
#
#
# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = SongsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('songs_home')
#         else:
#             error = "Invalid form"
#
#     form = SongsForm()
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'compositions/create.html', data)
#
#
# @login_required
# def profile(request):
#     # Add logic to retrieve and display user profile information
#     return render(request, 'main/profile.html')  # Replace 'main/profile.html' with your actual template
#
#
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('home')  # или любой другой URL после успешного входа
#     else:
#         form = AuthenticationForm()
#
#     return render(request, 'registration/login.html', {'form': form})
#
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user_profile = UserProfile.objects.create(user=user)
#             # Добавьте другие поля профиля при необходимости
#             return redirect('login')  # Имя вашего пути для входа
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     messages.success(request, 'Logout successful!')
#     return redirect('home')
#
#
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important to keep the user logged in
#             messages.success(request, 'Password changed successfully!')
#             return redirect('home')
#     else:
#         form = PasswordChangeForm(request.user)
#     return render(request, 'registration/change_password.html', {'form': form})
#
#
# # Create your views here.
# def index(request):
#     data = {
#         'title': 'Future Payments Systems',
#         'values': ['Future', 'Payments', 'Systems']
#     }
#     return render(request, 'main/main.html', data)
#
#
# def about(request):
#     return render(request, 'main/about.html')
#
#
# def contact(request):
#     return render(request, 'main/contact.html')
