//write a basic express boilerplate code
//express json middleware
const express = require("express");
const app = express();
app.use(express.json());
app.post("/todo",function(req, res){
	const createpayload = req.body;
	const parsepayload = createtodo.safeparse(createpayload);
	if (!parsepayload.success) {
		res.status(411).json({
			msg: "You sent the wrong inputs"
		})
		return;
	}
	//put it in mongodb
})

app.get("/todos",function(req, res){
})

app.put("/completed",function(req, res){
	const updatepayload = req.body;
	const parsepay:load = createtodo.safeparse(updatepayload);
	if (!parsepayload.success) {
		res.status(411).json({
			msg: "You sent the wrong inputs"
		})
		return;
	}
	//put it in mongodb

})
