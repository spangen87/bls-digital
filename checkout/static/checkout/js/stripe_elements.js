// Most logic from https://stripe.com/docs/payments/card-element?client=html
// and from Boutique Ado 

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements()
var style = {
  base: {
    color: "#151419",
    fontFamily: 'Arial, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#151419"
    }
  },
  invalid: {
    fontFamily: 'Arial, sans-serif',
    color: "#dc3545",
    iconColor: "#dc3545"
  }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');