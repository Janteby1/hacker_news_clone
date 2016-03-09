$(document).ready(function(){
  console.log("Hi there!")

  $('#comment').on('click', function(event){ //form submit event handler
    event.preventDefault();//prevents default which would reload page
    $('#submit_comment_div').text("Comment submitted!");

    // this is the value from the form 
    var comment = $('#comment_form #id_content').val()
    console.log(comment);

    var data = $("#comment_form").serialize() // returns all the data in your form
    console.log(data);


    // sending the data to the url then view
    $.ajax({
        method: "POST",
        url: ("/news/comment/" + $('#post_slug_thing').html()),
        data: data,
        // dataType: "jsonp", # only needed if we are going ot a different URL
        // alternative syntax
        // $.post( "/", $( "#grandpa_form" ).serialize(), function(data){

      // comes back from the view with a json respone to our data 
      success:function(response){
        console.log(response)
        // basicallly prints it out by attaching it to a div
        $('#comment_div').text(response["comment"])
        // $('.grandpa').empty();
        // $('.grandpa').append(response["msg"])
      }
    })
    console.log ($('#post_slug_thing').html());
  })
})



