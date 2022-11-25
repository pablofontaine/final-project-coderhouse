from django.core.exceptions import ValidationError
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from players.forms import TennisPlayerForm
from players.models import TennisPlayer

# Create your views here.

class TennisPlayersView(ListView):
    model = TennisPlayer
    template_name = 'players/players_list.html'
    # paginate_by = 3

class TennisPlayerCreateView(CreateView):
    model = TennisPlayer
    success_url = reverse_lazy('players:players-list')
    template_name = 'players/players_form.html'

    form_class = TennisPlayerForm

    def form_valid(self, form):
        data = form.cleaned_data
        actual_players = TennisPlayer.objects.filter(
            name=data['name'],
        ).count()

        if actual_players == 0:
            return super().form_valid(form)
        else:
            form.add_error('name', ValidationError("Este jugador ya existe"))
            return super().form_invalid(form)


class TennisPlayersDetailView(DetailView):
    model = TennisPlayer
    template_name = 'players/players_detail.html'
    fields = ['name', 'country', 'retired']


class TennisPlayerDeleteView(DeleteView):
    model = TennisPlayer
    template_name = 'players/players_confirm_delete.html'
    success_url = reverse_lazy('players:players-list')


class TennisPlayerUpdateView(UpdateView):
    model = TennisPlayer
    template_name = 'players/players_form.html'
    fields = ['name', 'country', 'retired']
    message_succes = 'Modificación exitosa'

    def get_success_url(self):
        player_id = self.kwargs["pk"]
        return reverse_lazy("players:players-detail", kwargs={"pk": player_id})
