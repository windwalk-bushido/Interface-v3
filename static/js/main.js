// Automatic dark or light mode
let light_mode_on = null;

function CheckMode() {
	if (localStorage.getItem('mode') === 'dark') {
		light_mode_on = false;
	} else {
		light_mode_on = true;
	}
}

let app_body = document.getElementById('body');
let btn_icon = document.getElementById('btn-icon');

function Render() {
	if (light_mode_on === true) {
		app_body.classList.remove('dark-bg');
		app_body.classList.add('light-bg');
		btn_icon.classList.remove('fa-sun');
		btn_icon.classList.add('fa-moon');
	} else {
		app_body.classList.remove('light-bg');
		app_body.classList.add('dark-bg');
		btn_icon.classList.remove('fa-moon');
		btn_icon.classList.add('fa-sun');
	}
}

function ChangeMode() {
	light_mode_on = !light_mode_on;
	if (light_mode_on === true) {
		localStorage.setItem('mode', 'light');
	} else {
		localStorage.setItem('mode', 'dark');
	}
	Render();
}

CheckMode();
Render();
