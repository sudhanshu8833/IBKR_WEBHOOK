from django.urls import path

from . import views

urlpatterns = [
    path("tradingview_webhook/", views.tradingview_webhook, name='tradingview_webhook'),
]