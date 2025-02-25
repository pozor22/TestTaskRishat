import stripe
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from testapi.models import Item, Order

from testtask.settings import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

class BuyItemAPIView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cancel/",
        )

        return Response({"session_id": session.id})


class BuyOrderView(APIView):
    def get(self, request, order_id):
        """Создаёт Stripe Checkout Session для заказа"""
        order = get_object_or_404(Order, id=order_id)
        line_items = []

        for item in order.items.all():
            line_items.append({
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": item.name},
                    "unit_amount": item.price,
                },
                "quantity": 1,
            })

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=line_items,
            mode="payment",
            success_url="http://127.0.0.1:8000/success/",
            cancel_url="http://127.0.0.1:8000/cancel/",
        )

        return Response({"session_id": session.id})