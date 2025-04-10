var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
      color: '#000',
      fontWeight: '500',
      fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
      fontSize: '16px',
      fontSmoothing: 'antialiased',
      '::placeholder': {
        color: 'd3d3d3',
      }
    },
    invalid: {
      iconColor: '#FFC7EE',
      color: '#FFC7EE',
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
  var errorDiv = document.getElementById('card-errors');
  if (event.error) {
    var html = `
      <span class='icon' role='alert'>
          <i class='fas fa-times'></i>
      </span>
      <span>${event.error.message}</span>
    `;
    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = '';
  }
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
  ev.preventDefault();
  card.update({'disabled': true});
  $('#submit-button').attr('disabled', true);
  $('#payment-form').fadeToggle(100);
  $('#loading-overlay').fadeToggle(100);

  var saveInfo = Boolean($('#id-save-info').attr('checked'));
  var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
  var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
  };
  var url = '/checkout/cache_checkout_data/';

  $.post(url, postData).done(function () {
    stripe.confirmCardPayment(clientSecret, {
      payment_method: {
        card: card,
          billing_details: {
            name: $.trim(form.full_name.value),
            email: $.trim(form.email.value),
            phone: $.trim(form.phone_number.value),
            address: {
              line1: $.trim(form.street_address1.value),
              line2: $.trim(form.street_address2.value),
              city: $.trim(form.town_or_city.value),
              state: $.trim(form.state.value),
              country: $.trim(form.country.value),
            }
          }
        },
        shipping: {
          name: $.trim(form.full_name.value),
          phone: $.trim(form.phone_number.value),
          address: {
            line1: $.trim(form.street_address1.value),
            line2: $.trim(form.street_address2.value),
            city: $.trim(form.town_or_city.value),
            state: $.trim(form.state.value),
            postal_code: $.trim(form.postcode.value),
            country: $.trim(form.country.value),
          }
        },
      }).then(function(result) {
        if (result.error) {
          var errorDiv = document.getElementById('card-errors');
          var html = `
            <span class='icon' role='alert'>
                <i class='fas fa-times'></i>
            </span>
            <span>${result.error.message}</span>`;
          $(errorDiv).html(html);
          $('#payment-form').fadeToggle(500);
          $('#loading-overlay').fadeToggle(500);
          card.update({'disabled': false});
          $('#submit-button').attr('disabled', false);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            form.submit();
          }
        }
      });
    }).fail(function () {
      location.reload();
    })
});