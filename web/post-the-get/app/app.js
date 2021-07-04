const express = require("express");
const path = require("path");

const app = express();

app.use(express.static(path.join(__dirname, "./public/css")));
app.use(express.static(path.join(__dirname, "./public/js")));

app.get("/", (req, res, nex) => {
	res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

app.get("/send", (req, res, next) => {
	res.sendFile(path.join(__dirname, 'views', 'gets.html'));

});

app.post("/send", (req, res, next) => {
	res.send("shellmates{7HE_w3B_is_w31RD}");
});

app.use((req, res) => {
	res.status(302).redirect("/");
});

app.listen(3000, () => {
	console.log('app listening on port 3000');
});
