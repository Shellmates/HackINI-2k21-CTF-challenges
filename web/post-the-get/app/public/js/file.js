let name = document.getElementById("name");
let address = document.getElementById("address");

function show() {
	document.getElementById("message").style.visibility = "visible";
	setTimeout(() => {
		document.getElementById("message").style.visibility = "hidden"
	}, 2000);
}
name.addEventListener("click", show);

address.addEventListener("click", show);
