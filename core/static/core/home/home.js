const exams = JSON.parse($("#exams").text());
const csrf_token = $("input[name=csrfmiddlewaretoken]").val()

setInterval(() => {
	for (var i=1; i<=exams.length; i++) {
		var li = $(`#${i}`);

		var delta = new Date(exams[i-1].due_date) - new Date()

		var days = Math.floor(delta / (1000 * 60 * 60 * 24)); 
		delta -= Math.floor(days * (1000 * 60 * 60 * 24))

		var hours = Math.floor(delta / (1000 * 60 * 60)); 
		delta -= Math.floor(hours * (1000 * 60 * 60))
		
		var minutes = Math.floor(delta / (1000 * 60)); 
		delta -= Math.floor(minutes * (1000 * 60))

		var seconds = Math.floor(delta / (1000));
		
		li.text(() => {
			return  `${days.toString().padStart(2, "0")}D:${hours.toString().padStart(2, "0")}H:${minutes.toString().padStart(2, "0")}M:${seconds.toString().padStart(2, "0")}S`;
		})
	}
}, 1000)

$("#submit").submit((e) => {
	e.preventDefault();
	$.ajax({
		type: 'POST',
		url: '/accounts/create/',
		data: {
			'email': $("#email").val(),
			'csrfmiddlewaretoken': csrf_token
		}, 
		success: (data) => {
			console.log(data)
		}
	})
})