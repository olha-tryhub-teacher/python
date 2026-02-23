from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Order


# список замовлень користувача
class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "shop/order_list.html"
    context_object_name = "orders"

    def get_queryset(self):
        return Order.objects.filter(
            client=self.request.user
        ).order_by("-created_at")


# деталі замовлення
class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "shop/order_detail.html"
    context_object_name = "order"

    def get_queryset(self):
        return Order.objects.filter(
            client=self.request.user
        )


# створення замовлення
class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    fields = ["comment"]
    template_name = "shop/order_create.html"
    success_url = reverse_lazy("order_list")

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)