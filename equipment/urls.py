from django.conf.urls import url

from .views import ArmorerShop, ArmorerShopBuyItem


urlpatterns = [
    url(r'^armorer$', ArmorerShop.as_view(), name='armorer'),
    url(r'^armorer/(?P<item_id>\d+)/buy', ArmorerShopBuyItem.as_view(), name='armorer-buy')
]
