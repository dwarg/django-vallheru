from django.views.generic import ListView, RedirectView
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Equipment


class ArmorerShop(ListView):
    model = Equipment
    template_name = 'equipment/armorer.html'
    queryset = Equipment.objects.filter(shop=True).order_by('eq_type', 'level')

    def get_queryset(self):
        queryset = super(ArmorerShop, self).get_queryset()
        return queryset


class ArmorerShopBuyItem(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        user = self.request.user
        item = Equipment.objects.get(id=kwargs['item_id'])
        if user.coins > item.cost:
            item.pk = None
            item.owner = user
            item.shop = False
            item.save()
            user.coins -= item.cost
            user.save()
            message = '%s został zakupiony i jest w twoim ekwipunku.' % item.name
            messages.add_message(self.request, messages.SUCCESS, message)
        else:
            message = 'Nie masz wystarczającej ilości monet by kupić %s.' % item.name
            messages.add_message(self.request, messages.WARNING, message)
        return reverse('equipment:armorer')
