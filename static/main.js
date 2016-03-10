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

      // comes back from the view with a json respone to our data 
      success:function(response){
        console.log(response)
        // basicallly prints it out by attaching it to a div
        $('#comment_div').text(response["comment"])
      }
    })

  })



    $('.comments_button').on('submit', function(event){
	event.preventDefault();

    var data = $(this).serialize() // returns all the data in your form
    console.log(data);
	console.log ("clicked!");

	$.ajax({
        method: "GET",
        url: ("/news/"),
        data: data,
        success: function(data){
        	console.log("here");
        	console.log(data)

// This will target the element with an id of list
// We use Mustache's "render" function to take the targeted template and load it with the data we got back earlier
// Use jQuery to target the div with the id of "blah" and change the inside of it's html with the variable of the rendered data
			var template = $('#list').html();
			// we get an object with a property comments, so here we call data.comments or just pass the data
			var renderM = Mustache.render(template,data);
			console.log(renderM);


			// if (typeof comments === 'undefined'){
			// 	console.log("There are no comments on this post");
			// }

			var comment_fk = (data.comments[0].post)
			var post = $("#" + comment_fk)

			// if (comment_fk === post) {
				post.html(renderM)
				
			}
		})
	})
});

