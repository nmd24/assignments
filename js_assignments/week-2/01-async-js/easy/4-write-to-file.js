const fs = require('fs');
const path = require('path');

// The path to the file you want to write to
const filePath = path.join(__dirname, '../file.txt');

// The content you want to write to the file
const content = "Hello, this is the content to write to the file.";

// Asynchronously write content to the file
fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log("File has been written successfully");
});

// You can add more code here that will run while the file is being written
