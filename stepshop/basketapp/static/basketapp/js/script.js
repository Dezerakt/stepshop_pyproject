// window.onload = function(){
//     $('.basket_list').on('click', 'input[type=number]', function(event){
//         let t_href = event.target;
//     })
// }

// $(document).ready(function () {
//     $('.basket_list').on('click', 'input[type=number]', function(event){
//         let t_href = event.target;

//         $.ajax({
//             url: "/basket/edit" + t_href.name + '/' + t_href.value + '/', 
//             success: function (data) {
//                 $('.basket_list').html(data.result)
//             }
//         });
//         event.preventDefault()
//     })
// });

$(document).ready(function () {
    const inp = $('.basket_list');
    function change_inp(t_href, current){
        $.ajax({
            url: "/basket/edit" + t_href.name + '/' + t_href.value + '/', 
            success: function (data) {
                if (t_href.value > 0){
                    $('.basket_summary').replaceWith(data.result)
                    current.parent().next().text('$' + data.product_total_price)
                } else {
                    current.parent().parent().detach();
                }
            },
        });
    }

    inp.on('click', 'input[type=number]', function(event){
        change_inp(event.target, $(this));
        
    })
});