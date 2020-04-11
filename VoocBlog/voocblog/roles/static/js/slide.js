$(document).ready(function() {
	setInterval(function(){
		$('#btn-next').trigger('click')
	},5000);

	$('#btn-next').click(function(event) {
		var slide_sau = $('.active').next();
		// console.log(slide_sau.length);
		var vi_tri_hien_tai = $('.active-nut').index()+1;
		console.log(vi_tri_hien_tai);
		if (slide_sau.length != 0) {
			$('.active').addClass('bien-mat-ben-trai').one('webkitAnimationEnd', function(event) {
				$('.bien-mat-ben-trai').removeClass('bien-mat-ben-trai').removeClass('active')
			});;
			slide_sau.addClass('active').addClass('di-vao-ben-phai').one('webkitAnimationEnd', function(event) {
				$('.di-vao-ben-phai').removeClass('di-vao-ben-phai')
			});;
			// xử lý nút
			$('.button-slide ul li').removeClass('active-nut');
			$('.button-slide ul li:nth-child('+(vi_tri_hien_tai+1)+')').addClass('active-nut');
		} else {
			$('.active').addClass('bien-mat-ben-trai').one('webkitAnimationEnd', function(event) {
				$('.bien-mat-ben-trai').removeClass('bien-mat-ben-trai').removeClass('active')
			});;
			$('.slide:first-child').addClass('active').addClass('di-vao-ben-phai').one('webkitAnimationEnd', function(event) {
				$('.di-vao-ben-phai').removeClass('di-vao-ben-phai')
			});;
			// xử lý nút
			$('.button-slide ul li').removeClass('active-nut');
			$('.button-slide ul li:nth-child(1)').addClass('active-nut');
		}
	});
	$('#btn-prev').click(function(event) {
		var slide_truoc = $('.active').prev();
		var vi_tri_hien_tai = $('.active-nut').index()+1;
		console.log(slide_truoc.length);
		if (slide_truoc.length != 0) {
			$('.active').addClass('bien-mat-ben-phai').one('webkitAnimationEnd', function(event) {
				$('.bien-mat-ben-phai').removeClass('bien-mat-ben-phai').removeClass('active');
			});;
			slide_truoc.addClass('active').addClass('di-vao-ben-trai').one('webkitAnimationEnd', function(event) {
				$('.di-vao-ben-trai').removeClass('di-vao-ben-trai');
			});;
			// xử lý nút
			$('.button-slide ul li').removeClass('active-nut');
			$('.button-slide ul li:nth-child('+(vi_tri_hien_tai-1)+')').addClass('active-nut');
		} else {
			$('.active').addClass('bien-mat-ben-phai').one('webkitAnimationEnd', function(event) {
				$('.bien-mat-ben-phai').removeClass('bien-mat-ben-phai').removeClass('active');
			});;
			$('.slide:last-child').addClass('active').addClass('di-vao-ben-trai').one('webkitAnimationEnd', function(event) {
				$('.di-vao-ben-trai').removeClass('di-vao-ben-trai');
			});;
			// xử lý nút
			$('.button-slide ul li').removeClass('active-nut');
			$('.button-slide ul li:last-child').addClass('active-nut');
		
		}
	});

	// $('button-slide ul li').click(function(event) {
	// 	var vi_tri_hien_tai = $('.active-nut').index()+1;
	// 	var vi_tri_click = $(this).index()+1;
	// 	$('.button-slide ul li').removeClass('active-nut');
	// 	$(this).removeClass('active-nut');
	// 		$('.active').addClass('bien-mat-ben-trai').one('webkitAnimationEnd', function(event) {
	// 			$('.bien-mat-ben-trai').removeClass('bien-mat-ben-trai').removeClass('active')
	// 		});;
	// 		$('.slide:nth-child('+vi_tri_click+')').addClass('active').addClass('di-vao-ben-phai').one('webkitAnimationEnd', function(event) {
	// 			$('.di-vao-ben-phai').removeClass('di-vao-ben-phai')
	// 		});;
	// });;

	$('.button-slide ul li').click(function(event) {
		var vi_tri_hien_tai = $('.active-nut').index()+1;
		var vi_tri_click = $(this).index()+1;
		$('.button-slide ul li').removeClass('active-nut');
		$(this).addClass('active-nut');
		if(vi_tri_click>vi_tri_hien_tai){
			$('.active').addClass('bien-mat-ben-trai').one('webkitAnimationEnd', function(event) {
				$('.bien-mat-ben-trai').removeClass('bien-mat-ben-trai').removeClass('active');
			});;
			$('.slide:nth-child('+vi_tri_click+')').addClass('active').addClass('di-vao-ben-phai').one('webkitAnimationEnd', function(event) {
				$('.di-vao-ben-phai').removeClass('di-vao-ben-phai');
			});;
		}
		if(vi_tri_click<vi_tri_hien_tai){
			$('.active').addClass('bien-mat-ben-phai').one('webkitAnimationEnd', function(event) {
				$('.bien-mat-ben-phai').removeClass('bien-mat-ben-phai').removeClass('active');
			});;
			$('.slide:nth-child('+vi_tri_click+')').addClass('active').addClass('di-vao-ben-trai').one('webkitAnimationEnd', function(event) {
				$('.di-vao-ben-trai').removeClass('di-vao-ben-trai');
			});;
		}

	});
});