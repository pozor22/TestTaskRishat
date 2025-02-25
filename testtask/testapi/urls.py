from django.urls import path

from . import views

from .api import APIViews

urlpatterns = [
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path("buy/<int:item_id>/", APIViews.BuyItemAPIView.as_view(), name="buy_item"),
]