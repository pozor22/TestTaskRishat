from django.views.generic import DetailView

from testtask.config import STRIPE_PUBLIC_KEY

from .models import Item, Order


class ItemDetailView(DetailView):
    model = Item
    template_name = "testapi/item_detail.html"
    context_object_name = "item"
    extra_context = {"stripe_public_key": STRIPE_PUBLIC_KEY}


class OrderDetailView(DetailView):
    model = Order
    template_name = "testapi/order_detail.html"
    context_object_name = "order"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["stripe_public_key"] = STRIPE_PUBLIC_KEY
        return context
