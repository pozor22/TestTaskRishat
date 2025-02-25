from django.urls import path

from . import views

from .api import APIViews

urlpatterns = [
    # Templates
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='item_detail'),

    # API
    path("buy/<int:item_id>/", APIViews.BuyItemAPIView.as_view(), name="buy_item"),
    path("buy_order/<int:order_id>/", APIViews.BuyOrderView.as_view(), name="buy_order"),
]