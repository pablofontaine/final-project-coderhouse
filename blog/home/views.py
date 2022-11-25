from django.contrib import messages
from django.shortcuts import render, redirect
from home.forms import UserRegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy



# Create your views here.


def index(request):
    return render(
        request=request,
        context=dict(),
        template_name="home/index.html",
    )


def register(request):

    form = UserRegisterForm(
        request.POST) if request.POST else UserRegisterForm()

    # if method POST, si el usuario está enviando el formulario
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "¡Usuario creado exitosamente!")
            return redirect("login")

    # else method GET, si el usario solicita para registrarse
    return render(
        request=request,
        context={"form": form, },
        template_name="registration/register.html",
    )

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'registration/user_detail.html'
    fields = ['fist_name', 'last_name', 'email']

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/user_update.html'
    fields = ['first_name','last_name','email']
    message_succes = 'Modificación exitosa'

    def get_success_url(self):
        user_id = self.kwargs["pk"]
        return reverse_lazy("players:users-detail", kwargs={"pk": user_id})

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'registration/user_confirm_delete.html'
    success_url = reverse_lazy('home:index')