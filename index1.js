const express = require('express');

const app = express();

const users = [{
    name : "nikhil",
    phonenumber : [{healthy: false}]
    }]


app.get('/', function(req, res) {
    const nikhilphonenumbers = users[0].phonenumber;
    const numberofphonnumbers = nikhilphonenumbers.length;
    let totalphonenumH = 0;
    for (let i = 0; i < nikhilphonenumbers.length; i++) {
        if (totalphonenumH[i].phonenumber){
            totalphonenumH += 1;}
}
    const totalphonenumUH = numberofphonnumbers - totalphonenumH;
    res.json({
        nikhilphonenumbers,
        totalphonenumH,
        totalphonenumUH
    })
})
app.listen(3001); 