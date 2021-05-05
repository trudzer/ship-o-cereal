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
});