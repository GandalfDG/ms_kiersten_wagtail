from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse

import stripe

stripe.api_key = None

# Create your views here.
def stripe_purchase_deposit(request):
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1RtcIpPDRJagoS8D8H9org9U',
                    'quantity': 1
                }
            ],
            mode='payment',
            success_url="http://google.com",
            cancel_url="http://google.com"
        )
    except Exception as e:
        return HttpResponse(e)
    
    return HttpResponseRedirect(checkout_session.url)
