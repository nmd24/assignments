const fs = require('fs');
const path = require('path');

// Construct the file path relative to the script location
const filePath = path.join(__dirname, 'output.txt');

// Asynchronous file read
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log("File content:", data);
});

// Simulate an expensive operation
function expensiveOperation() {
    let start = new Date();
    let end = start;

    // Loop for a certain amount of time to simulate a heavy task
    while (end - start < 2000) { // 10,000 milliseconds or 10 seconds
        end = new Date();
    }

    console.log("Expensive operation completed");
}

expensiveOperation();