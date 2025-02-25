from django.views.generic import DetailView

from testtask.config import STRIPE_PUBLIC_KEY

from .models import Item


class ItemDetailView(DetailView):
    model = Item
    template_name = "testapi/item_detail.html"
    context_object_name = "item"
    extra_context = {"stripe_public_key": STRIPE_PUBLIC_KEY}
