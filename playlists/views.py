import json
from django.shortcuts import render, redirect
from .forms import PlaylistForm

INITIAL_PLAYLISTS = [
    {'title': 'Rock Classics', 'genre': 'Rock', 'description': 'Лучшие рок-хиты 80-х и 90-х'},
    {'title': 'Chill Vibes', 'genre': 'Lo-Fi', 'description': 'Расслабляющая музыка для учебы'},
]

COOKIE_NAME = 'user_playlists'


def _get_user_playlists(request):
    """Читает список плейлистов пользователя из куки."""
    raw = request.COOKIES.get(COOKIE_NAME, '[]')
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return []


def playlist_list(request):
    """Главная: начальные + пользовательские плейлисты."""
    user_playlists = _get_user_playlists(request)
    all_playlists = INITIAL_PLAYLISTS + user_playlists
    return render(request, 'playlists/index.html', {'playlists': all_playlists})


def playlist_create(request):
    if request.method == 'POST':
        form = PlaylistForm(request.POST)
        if form.is_valid():
            user_playlists = _get_user_playlists(request)
            user_playlists.append({
                'title': form.cleaned_data['title'],
                'genre': form.cleaned_data['genre'],
                'description': form.cleaned_data['description'],
            })
            response = redirect('playlist_list')
            response.set_cookie(
                COOKIE_NAME,
                json.dumps(user_playlists),
                max_age=60 * 60 * 24 * 30,  # 30 дней
                path='/',
            )
            return response
    else:
        form = PlaylistForm()
    return render(request, 'playlists/create.html', {'form': form})