from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhooks
    Credits to Boutique Ado Walkthrough
    """
    def __init__(self, event):
        self.request = request

    def handle_event(self, event):
        """
        Handle a unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook recieved: {event["type"]}',
            status=200)
