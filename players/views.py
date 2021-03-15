# -*- encoding: utf-8 -*-
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, View

from players.models import PlayerRace
from .utils import get_client_ip


class StatisticView(LoginRequiredMixin, TemplateView):
    template_name = 'account/statistic.html'

    def get_context_data(self, **kwargs):
        context = super(StatisticView, self).get_context_data(**kwargs)
        context['player'] = self.request.user
        context['ip'] = get_client_ip(self.request)
        return context


class RaceView(LoginRequiredMixin, ListView):
    template_name = 'players/race.html'
    model = PlayerRace
    context_object_name = 'races'

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.race is not None:
            messages.add_message(self.request, messages.WARNING, 'Już wybrałeś swoją rasę!')
            return redirect('player:statistic')

        return super(RaceView, self).render_to_response(context)


class ChosenRaceView(LoginRequiredMixin, View):
    http_method_names = [u'post']

    def post(self, request, *args, **kwargs):
        if request.user.race is None:
            user = request.user
            user.race = get_object_or_404(PlayerRace, pk=kwargs.get('pk'))
            user.save()
        else:
            messages.add_message(request, messages.WARNING, 'Już wybrałeś swoją rasę!')
        return redirect(reverse('player:statistic'))