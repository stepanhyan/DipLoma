from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db import transaction  # Import the transaction module
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from compositions.forms import SongsForm
from compositions.models import Comment
from main.forms import SignUpForm
from .forms import CommentForm
from .forms import LikeForm
from .models import Songs, UserProfile, Like


@require_POST
def like_song(request):
    form = LikeForm(request.POST)

    if form.is_valid():
        song_id = form.cleaned_data['song_id']
        song = get_object_or_404(Songs, id=song_id)

        if request.user.is_authenticated:
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)

            with transaction.atomic():  # Use a database transaction to ensure consistency
                if Like.objects.filter(user=user_profile, song=song).exists():
                    Like.objects.filter(user=user_profile, song=song).delete()
                    song.likes_users.remove(user_profile)
                    print("User unliked the song")
                else:
                    Like.objects.create(user=user_profile, song=song)
                    print("User liked the song")
                    song.likes_users.add(user_profile)  # Add the liked user to the song's likes_users field

                likes_count = song.likes_users.count()
                print('likes count', likes_count)

                return JsonResponse({'status': 'success', 'likes': likes_count, 'is_liked': True, 'action': 'liked'})

        else:
            return JsonResponse({'status': 'error', 'message': 'User not authenticated'})
    else:
        print(form.errors)
        return JsonResponse({'status': 'error', 'message': 'Invalid form data', 'errors': form.errors})


@require_POST
def post_comment(request):
    user_profile = UserProfile.objects.get(user=request.user)
    form = CommentForm(request.POST)

    if form.is_valid():
        song_id = request.POST.get('song_id')
        comment_text = form.cleaned_data['comment']
        print('song id -', song_id)
        print('comment text -', comment_text)

        if song_id and comment_text:
            song = Songs.objects.get(id=song_id)
            comment = Comment.objects.create(user=user_profile, song=song, text=comment_text)

            # Return additional information in the response
            response_data = {
                'status': 'success',
                'comments': song.comment_set.count(),
                'comment': {
                    'user': request.user.username,
                    'text': comment.text,
                },
            }
            return JsonResponse(response_data)
        else:
            print('form is not valid')
            response_data = {'status': 'error', 'message': 'Invalid form data'}
    else:
        print('form is not valid ape jan')
        response_data = {'status': 'error', 'message': 'Invalid form data'}

    return JsonResponse(response_data)


def artist_detail(request, artist_id):
    artist = get_object_or_404(Songs, id=artist_id)
    return render(request, 'compositions/artist_detail.html', {'artist': artist})


def songs_home(request):
    compositions = Songs.objects.all()
    return render(request, 'compositions/songs.html', {'compositions': compositions})


def create(request):
    error = ''
    if request.method == 'POST':
        form = SongsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('songs_home')
        else:
            error = "Invalid form"

    form = SongsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'compositions/create.html', data)


@login_required
def profile(request):
    # Add logic to retrieve and display user profile information
    return render(request, 'registration/profile.html')  # Replace 'main/profile.html' with your actual template


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect('home')  # или любой другой URL после успешного входа
        else:
            form = AuthenticationForm()

        return render(request, 'registration/login.html', {'form': form})
    else:
        return render(request, 'registration/profile.html')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user_profile = UserProfile.objects.create(user=user)
                # Добавьте другие поля профиля при необходимости
                return redirect('login')  # Имя вашего пути для входа
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})
    else:
        return render(request, 'registration/profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Password changed successfully!')
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})


def home_view(request):
    data = {
        'title': 'Future Payments Systems',
        'values': ['Future', 'Payments', 'Systems']
    }
    return render(request, 'main/main.html', data)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
