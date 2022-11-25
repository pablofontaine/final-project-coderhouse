from django.urls import path

from players import views

app_name = 'players'
urlpatterns = [
    path('list_players/', views.TennisPlayersView.as_view(), name='players-list'),
    path('list_players/create/', views.TennisPlayerCreateView.as_view(), name='players-add'),
    path('list_players/<int:pk>/detail/', views.TennisPlayersDetailView.as_view(), name='players-detail'),
    path('list_players/<int:pk>/update/', views.TennisPlayerUpdateView.as_view(), name='players-update'),
    path('list_players/<int:pk>/delete/', views.TennisPlayerDeleteView.as_view(), name='players-delete'),
]