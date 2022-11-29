from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, path
from home import views

app_name = 'home'
urlpatterns = [
    # News views
    path('', views.NewListView.as_view(), name="index"),
    path('news/add/', views.NewCreationView.as_view(), name="new-add"),
    path('news/<int:pk>/detail', views.NewDetailView.as_view(), name="new-detail"),
    path('news/<int:pk>/update', views.NewUpdateView.as_view(), name="new-update"),
    path('news/<int:pk>/delete', views.NewDeleteView.as_view(), name="new-delete"),
    # Accounts views
    path('accounts/register/', views.register, name="user-register"),
    path('accounts/register/<int:pk>/update',
         views.UserUpdateView.as_view(), name='user-update'),
    path('accounts/register/<int:pk>/detail',
         views.UserDetailView.as_view(), name='user-detail'),
    path('accounts/register/<int:pk>/delete',
         views.UserDeleteView.as_view(), name='user-delete'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='registration/user_password_change.html',
        success_url=reverse_lazy('home:password-done'),
    ), name='password-change'),
    path('accounts/password_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='registration/user_password_done.html',
    ), name='password-done'),
    # Other views
    path('about/', views.about, name='about'),
    path('avatar/load/', views.avatar, name="avatar"),
    path('routes/', views.list_paths, name='list-paths')
]
