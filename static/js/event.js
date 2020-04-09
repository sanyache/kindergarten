$(document).ready(function(){
    function loadMore(){
        var page = 1;
        $('a.load-more').click(function(event){ 
            var link = location.href;
            var num_pages = $(this).data('pages');
            page += 1;
            if( page <= num_pages){
                link =  link+"?page="+ page;
                    $.ajax({
                    'url': link,
                    'dataType': 'html',
                    'type': 'get',
                    'success': function(data, status, xhr){ 
                        html = $(data).find('.items');
                        $('.pages').append(html);
                    
                    }
                });
            } 
            if( page == num_pages ){
                $(this).hide();
            }
            return false;
         });
    
    }

    loadMore();

});