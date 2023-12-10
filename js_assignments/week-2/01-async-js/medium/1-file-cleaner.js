const fs = require('fs');
const path = require('path');

// Path to the file
const filePath = path.join(__dirname, 'myfile.txt');

// Read the file
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    // Remove extra spaces
    const cleanedData = data.replace(/\s+/g, ' ');

    // Write the cleaned data back to the file
    fs.writeFile(filePath, cleanedData, 'utf8', (err) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log("File cleaned and written successfully");
    });
});
