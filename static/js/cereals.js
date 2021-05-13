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