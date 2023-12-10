const fs = require('fs');
const path = require('path');

// The path to the file you want to append to
const filePath = path.join(__dirname, 'output.txt');

// The content you want to append to the file
const content = "I am working on these assignments right now.\n";

// Asynchronously append content to the file
fs.appendFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log("Content appended to file successfully");
});

// You can add more code here that will run while the file is being written
