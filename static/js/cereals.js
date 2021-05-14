function search_item(){
    var searchText = $('#search-box').val();
      $.ajax({
          url:  '/cereals?search_filter=' + searchText,
          type: 'GET',
          success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well cereal">
                                <a href="/cereals/${d.id}">
                                    <img class="cereal-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                                <a href="/cereals/${d.id}">
                                    <button type="submit" class="btn btn-primary pull-right" style="clear:both; margin: 10px 0">More Information</button>
                                </a>
                                <a href="/cart/add_to_cart/${d.id}">
                                <button type="submit" class="btn btn-primary pull-right" style="clear:both; margin: 10px 0">Buy $${d.price}</button>
                                </a>
                                <p>Copyright © 2021 Ship O'Cereal</p>
                           </div>`
                });
                $('.cereals').html(newHtml.join(''));
                $('#search-box').val('');
          },
          error: function (xhr, status, error) {
              console.error(error);
          }
      })
    };

function price_item(){
    var price_box_1 = $('#price-box').val();
    var price_box_2 = $('#price-box-2').val();
      $.ajax({
          url:  '/cereals?price_start=' + price_box_1 + "&price_end=" + price_box_2,
          type: 'GET',
          success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well cereal">
                                <a href="/cereals/${d.id}">
                                    <img class="cereal-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                                <a href="/cereals/${d.id}">
                                    <button type="submit" class="btn btn-primary pull-right" style="clear:both; margin: 10px 0">More Information</button>
                                </a>
                                <a href="/cart/add_to_cart/${d.id}">
                                <button type="submit" class="btn btn-primary pull-right" style="clear:both; margin: 10px 0">Buy $${d.price}</button>
                                </a>
                                <p>Copyright © 2021 Ship O'Cereal</p>
                           </div>`
                });
                $('.cereals').html(newHtml.join(''));
                $('#search-box').val('');
          },
          error: function (xhr, status, error) {
              console.error(error);
          }
      })
    };

function search_button(category){
      $.ajax({
          url:  '/cereals?category_filter=' + category,
          type: 'GET',
          success: function (resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="well cereal">
                                <a href="/cereals/${d.id}">
                                    <img class="cereal-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                                <a href="/cereals/${d.id}">
                                    <button type="submit" class="btn btn-primary pull-right" style="clear:both; margin: 10px 0">More Information</button>
                                </a>
                                <a href="/cart/add_to_cart/${d.id}">
                                <button type="submit" class="btn btn-primary pull-right" style="clear:both; margin: 10px 0">Buy $${d.price}</button>
                                </a>
                                <p>Copyright © 2021 Ship O'Cereal</p>
                           </div>`
                });
                $('.cereals').html(newHtml.join(''));
                $('#search-box').val('');
          },
          error: function (xhr, status, error) {
              console.error(error);
          }
      })
    };

$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
            search_item();
    });

    $('#search-box').keypress(function(e) {
        if (e.which === 13) {
            e.preventDefault();
            search_item();
        }
    });

    $('#vegan-button').on('click', function(e) {
        e.preventDefault();
            search_button(1);
    });

    $('#wheat-button').on('click', function(e) {
        e.preventDefault();
            search_button(2);
    });

    $('#oats-button').on('click', function(e) {
        e.preventDefault();
            search_button(3);
    });

    $('#sugary-button').on('click', function(e) {
        e.preventDefault();
            search_button(4);
    });

    $('#price-btn').on('click', function(e) {
        e.preventDefault();
            price_item();
    });

    $('#price-box').keypress(function(e) {
        if (e.which === 13) {
            e.preventDefault();
            price_item();
        }
    });

    $('#price-box-2').keypress(function(e) {
        if (e.which === 13) {
            e.preventDefault();
            price_item();
        }
    });
});


var stripe = Stripe('pk_test_51IqzhLEi4iZpiAj5tN51zOyrKQj5qA7dzI61uJgXq0RLYhfiS5OYavpFyOj2RWzhjt3BaxjykSo1yv3eNYoa8K8G008EnL5WxG');

// Create an instance of Elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
base: {
  fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
  fontSmoothing: 'antialiased',
  fontSize: '16px',
  '::placeholder': {
    color: '#aab7c4'
  }
},
invalid: {
  color: '#fa755a',
  iconColor: '#fa755a'
}
};

// Create an instance of the card Element.
var card = elements.create('card', {style: style});

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function(event) {
var displayError = document.getElementById('card-errors');
if (event.error) {
  displayError.textContent = event.error.message;
} else {
  displayError.textContent = '';
}
});

// Handle form submission.
var form = document.getElementById('stripe-form');
form.addEventListener('submit', function(event) {
event.preventDefault();

stripe.createToken(card).then(function(result) {
  if (result.error) {
    // Inform the user if there was an error.
    var errorElement = document.getElementById('card-errors');
    errorElement.textContent = result.error.message;
  } else {
    // Send the token to your server.
    stripeTokenHandler(result.token);
  }
});
});

// Submit the form with the token ID.
function stripeTokenHandler(token) {
// Insert the token ID into the form so it gets submitted to the server
var form = document.getElementById('stripe-form');
var hiddenInput = document.createElement('input');
hiddenInput.setAttribute('type', 'hidden');
hiddenInput.setAttribute('name', 'stripeToken');
hiddenInput.setAttribute('value', token.id);
form.appendChild(hiddenInput);

// Submit the form
form.submit();
}

var currentCardForm = $('.current-card-form');
var newCardForm = $('.new-card-form');
var use_default_card = document.querySelector("input[name=use_default_card]");
use_default_card.addEventListener('change', function() {
if (this.checked) {
  newCardForm.hide();
  currentCardForm.show()
} else {
  newCardForm.show();
  currentCardForm.hide()
}
})