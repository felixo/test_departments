var csrf_token = $('meta[name="csrf-token"]').attr('content');
$.ajaxPrefilter(function(options, originalOptions, jqXHR){
    if (options.type.toLowerCase() === "post") {
        // initialize `data` to empty string if it does not exist
        options.data = options.data || "";

        // add leading ampersand if `data` is non-empty
        options.data += options.data?"&":"";

        // add _token entry
        options.data += "_token=" + encodeURIComponent(csrf_token);
    }
});

function get_table(url){
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                             break;
                         }
                     }
                 }
                 return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         }
    });
    var jqxhr = $.get(url, function() {
    })
    .done(function(data) {
        var thead = ['Название департамента', 'Удалить'];
        $('.table_head').empty();
        jQuery.each(thead, function(index, item) {
            $('.table_head').append('<th>'+item+'</th>');
        });
        $('.table_body').empty();

        if (data.links.prev != null) {
            $('.content').append('<button type="button" class="btn btn-primary prev">Предыдущая страница</button>');
            $('.prev').click(function(){
                $('.next').remove();
                $('.prev').remove();
                get_table(data.links.prev);
            });
        }
        if (data.links.next != null) {
            $('.content').append('<button type="button" class="btn btn-primary next">Следущая страница</button>');
            $('.next').click(function(){
                $('.next').remove();
                $('.prev').remove();
                get_table(data.links.next);
            });
        }

        jQuery.each(data.data, function(index, item) {
            var del_butt = '<button type="button" class="btn btn-primary department_click" data-toggle="modal" data-target="#exampleModal" data-id="'+item.id+'">Удалить</button>'
            $('.table_body').append('<tr><td>'+item.attributes.title+'</td><td>'+del_butt+'</td></tr>');
        });
        $('.department_click').click(function(){
            var dep_id = $(this).data('id');
            $('.dep_delete').click(function(){
                $.ajax({
                  method: "DELETE",
                  url: "api/delete_dep/"+dep_id+"/",
                })
                  .done(function( msg ) {
                    $('#exampleModal').modal('hide');
                    $('.next').remove();
                    $('.prev').remove();
                    get_table('api/departments');
                  });
            });
        });
    })
    .fail(function() {
        alert( "ajax error" );
    })
    .always(function() {
    });
 };

 function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
};

function add_department(){
    $('.dep_add').click(function(){
        var dep_title = $('#dep_title').val()
        console.log(dep_title);
        $.ajax({
                  method: "POST",
                  url: "api/departments",
                  data: { "title": dep_title},
                })
                  .done(function( msg ) {
                    $('#add_dep').modal('hide');
                    $('.next').remove();
                    $('.prev').remove();
                    get_table('api/departments');
                  });
    });
};

function get_table_worker(url){
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                         if (cookie.substring(0, name.length + 1) == (name + '=')) {
                             cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                             break;
                         }
                     }
                 }
                 return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         }
    });
    var jqxhr = $.get(url, function() {
    })
    .done(function(data) {
        var thead = ['ФИО', 'Телефон', 'Оклад', 'Удалить'];
        $('.table_head').empty();
        jQuery.each(thead, function(index, item) {
            $('.table_head').append('<th>'+item+'</th>');
        });
        $('.table_body').empty();

        if (data.links.prev != null) {
            $('.content').append('<button type="button" class="btn btn-primary prev">Предыдущая страница</button>');
            $('.prev').click(function(){
                $('.next').remove();
                $('.prev').remove();
                get_table_worker(data.links.prev);
            });
        }
        if (data.links.next != null) {
            $('.content').append('<button type="button" class="btn btn-primary next">Следущая страница</button>');
            $('.next').click(function(){
                $('.next').remove();
                $('.prev').remove();
                get_table_worker(data.links.next);
            });
        }

        jQuery.each(data.data, function(index, item) {
            var del_butt = '<button type="button" class="btn btn-primary department_click" data-toggle="modal" data-target="#exampleModal" data-id="'+item.id+'">Удалить</button>'
            $('.table_body').append('<tr><td>'+item.attributes.fio+'</td><td>'+item.attributes.phone+'</td><td>'+item.attributes.sellery+' р.</td><td>'+del_butt+'</td></tr>');
        });
        $('.department_click').click(function(){
            var dep_id = $(this).data('id');
            $('.worker_delete').click(function(){
                $.ajax({
                  method: "DELETE",
                  url: "api/delete_worker/"+dep_id+"/",
                })
                  .done(function( msg ) {
                    $('#exampleModal').modal('hide');
                    $('.next').remove();
                    $('.prev').remove();
                    get_table_worker('api/workers');
                  });
            });
        });
    })
    .fail(function() {
        alert( "ajax error" );
    })
    .always(function() {
    });
 };

 function add_worker(){
    $('.worker_add').click(function(){
        var dep_title = '{"type": "Department", "id": '+$('#dep_select').val()+'}';
        var worker_fio = $('#worker_fio').val()
        var worker_phone = $('#worker_phone').val()
        var worker_sellery = $('#worker_sellery').val()
        $.ajax({
                  method: "POST",
                  url: "api/workers",
                  data: { "fio": worker_fio, "phone": worker_phone, "sellery": worker_sellery, "department": dep_title},
                })
                  .done(function( msg ) {
                    $('#add_worker').modal('hide');
                    $('.next').remove();
                    $('.prev').remove();
                    get_table_worker('api/workers');
                  });
    });
};