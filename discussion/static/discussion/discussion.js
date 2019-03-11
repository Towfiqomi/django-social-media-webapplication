
let reload_discussion_id = 0;
if (document.title === 'Discussion'){
    let timer = window.setInterval(function() {

            message_sending_view(reload_discussion_id);

        }, 5000);
}


$(document).ready(function () {
    reload_discussion_id = $('#discussion_id').val();

    $('body').on('click', '#message_send', function (e) {
       let discussion_id= $('#discussion_id').val();
       let message_text= $('#message_text').val();

       $.ajax(
           {
               type : 'GET',
               url: '/message_save?discussion_id='+ discussion_id + '&message_text='+message_text,

               success:function (response) {

                if (response==='1'){
                    console.log(response);

                    message_sending_view(discussion_id);




                }
               }
           }
       ) 
    });
    $('body').on('click', '.delete_message', function () {
       let discussion_id= $(this).data('discussion_id');
       let message_id = $(this).data('message_id');

       $.ajax(
           {
               type : 'GET',
               url: '/message_delete_view?discussion_id='+ discussion_id + '&message_id='+message_id,

               success:function (response) {

                if (response==='1'){
                    console.log(response);

                    message_sending_view(discussion_id);

                }
               }
           }
       )
    });


});



function message_sending_view(discussion_id) {
    $.ajax(
           {
               type : 'GET',
               url: '/message_save_view?discussion_id='+ discussion_id,
               success:function (response) {
                 $('.mesgs').html(response);
               }
           }
       );
}



















