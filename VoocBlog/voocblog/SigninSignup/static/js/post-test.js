	function show_post(){
	    $("#text-area").css("display","none");
	    $("#abc").fadeIn();
	}
	function hide_post(){
	    $("#abc").css("display","none");
	    $("#text-area").fadeIn();
	}

$(document).ready(function() {

	$('.bg-nav-bar a').on('click', function(event) {
		event.preventDefault();
		/* Act on the event */
		part = $(this).attr('href');

		position = $(part).offset().top;

		$('html, body').animate({scrollTop:position}, 1400);
	});
});