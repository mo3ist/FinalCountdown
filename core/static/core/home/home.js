const exams = JSON.parse($("#exams").text());
const csrf_token = $("input[name=csrfmiddlewaretoken]").val()

setInterval(() => {
	for (var i=1; i<=exams.length; i++) {
		var li = $(`#${i}`);
		var daysElement = $(`#days-${i}`)
		var hoursElement = $(`#hours-${i}`)
		var minutesElement = $(`#minutes-${i}`)
		var secondsElement = $(`#seconds-${i}`)

		var delta = new Date(exams[i-1].due_date) - new Date()

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
	}
}, 1000)

$("#sub").click((e) => {
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url: '/accounts/subscripe/',
		data: {
			'email': $("#email").val(),
			'csrfmiddlewaretoken': csrf_token
		}, 
		success: (data) => {

			// Yeah, reloading with the current technologies
			// I use it so bad that it's actually funny
			
			// But I don't have the time
			location.reload()
		}
	})
})

$("#unsub").click((e) => {
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url: '/accounts/unsubscripe/',
		data: {
			'email': $("#email").val(),
			'csrfmiddlewaretoken': csrf_token
		}, 
		success: (data) => {
			location.reload()
		}
	})
})



// Hide carousel controls on first and last 
$('#carousel').on('slid', '', checkitem);  // on caroussel move
$('#carousel').on('slid.bs.carousel', '', checkitem); // on carousel move

$(document).ready(function(){               // on document ready
    checkitem();
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