from django.urls import path
from .views import stripe_purchase_deposit

urlpatterns = [
    path("purchase/", stripe_purchase_deposit)
]