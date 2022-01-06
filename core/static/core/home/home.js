const exams = JSON.parse($("#exams").text());

const timer = (initial=false) => {
	for (var i=1; i<=exams.length; i++) {
		var li = $(`#${i}`);
		var daysElement = $(`#days-${i}`)
		var hoursElement = $(`#hours-${i}`)
		var minutesElement = $(`#minutes-${i}`)
		var secondsElement = $(`#seconds-${i}`)

		var delta = new Date(exams[i-1].due_date) - new Date()
		if (delta > 0) {
			var days = Math.floor(delta / (1000 * 60 * 60 * 24)); 
			delta -= Math.floor(days * (1000 * 60 * 60 * 24))
	
			var hours = Math.floor(delta / (1000 * 60 * 60)); 
			delta -= Math.floor(hours * (1000 * 60 * 60))
			
			var minutes = Math.floor(delta / (1000 * 60)); 
			delta -= Math.floor(minutes * (1000 * 60))
	
			var seconds = Math.floor(delta / (1000));
			
			daysElement.text(() => {return days.toString().padStart(2, "0")})
			hoursElement.text(() => {return hours.toString().padStart(2, "0")})
			minutesElement.text(() => {return minutes.toString().padStart(2, "0")})
			secondsElement.text(() => {return seconds.toString().padStart(2, "0")})
		} else {
			if (initial) {
				var og_image = $(`#image-${i}`).attr('src')
	
				$(`#image-${i}`).attr('src', '/static/core/home/wasted.png')
				$(`#image-${i}`).css('background-image', `url(${og_image})`)
				$(`#image-${i}`).css('background-repeat', 'no-repeat')
				$(`#image-${i}`).css('background-size', 'contain')
				$(`#image-${i}`).css('opacity', '0.75')

			}
		}
	}
}

setInterval(() => {
	timer()
}, 1000)

$("#form").submit((e) => {
	e.preventDefault()

	const validateEmail = (email) => {
	return String(email)
		.toLowerCase()
		.match(
		/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
		);
	};

	if ( validateEmail($("#email").val()) ){
		if ( $('#sub').length > 0 ) {
			var csrf_token = readCookie("csrftoken")
	
			$.ajax({
				type: 'POST',
				url: '/accounts/subscripe/',
				headers: {'X-CSRFToken': csrf_token},
				data: {
					'email': $("#email").val(),
				}, 
				success: (data) => {
					// // Replace with unsub
					// $("#button-wrapper").html(`
					// 	<button
					// 		id="unsub"
					// 		class="w-100 text-center btn btn-danger form-item"
					// 	>
					// 		😫 خلاص يسطا مش قادر 
					// 	</button>
					// `)
	
					// I Don't want a 'toggle' cause people will spam it. Instead, I'll render a 'Done'
					
					$('form').html(`
						<div class="w-100 h-100 d-flex justify-content-center align-items-center" style="border-radius: 20px;">
							<h3 class="text-center"> 🙆 اوكي </h3>	
						<div/>
					`)
				}
			})
	
		} else if ( $('#unsub').length > 0 ) {
			var csrf_token = readCookie("csrftoken")
	
			$.ajax({
				type: 'POST',
				url: '/accounts/unsubscripe/',
				headers: {'X-CSRFToken': csrf_token},
				data: {
					'email': $("#email").val(),
				}, 
				success: (data) => {
					// Replace with sub
					$("#button-wrapper").html(`
						<button
							id="sub"
							class="w-100 btn btn-success rounded-3 form-item"
						>
							🔔 فكرني اني بائس
						</button>
					`)
					$("#email").val("")
				}
			})
		}
	} else {
		$("#email").focus()
		$("#email").css("outline", "2px solid red")
	}

	

})


function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Hide carousel controls on first and last 
$('#carousel').on('slid', '', checkitem);  // on caroussel move
$('#carousel').on('slid.bs.carousel', '', checkitem); // on carousel move

$(document).ready(function(){               // on document ready
    checkitem();
	timer(true);
});

function checkitem()                        // check function
{
    var $this = $('#carousel');
    if($('.carousel-inner .carousel-item:first').hasClass('active')) {
        $this.children('.carousel-control-prev').hide();
        $this.children('.carousel-control-next').show();
    } else if($('.carousel-inner .carousel-item:last').hasClass('active')) {
        $this.children('.carousel-control-next').hide();
        $this.children('.carousel-control-prev').show();
    } else {
        $this.children('.carousel-control-prev').show();
        $this.children('.carousel-control-next').show();
    } 
}