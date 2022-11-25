from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy, path
from django.http import HttpRequest
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name="index"),
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
]
