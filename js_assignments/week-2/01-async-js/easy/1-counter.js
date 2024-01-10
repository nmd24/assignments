let counter = 0; // Starting point of the counter

// Function to update the counter
function updateCounter() {
    counter += 1;
    console.log(counter);
}

// Set interval to call updateCounter function every 1000 milliseconds (1 second)
setInterval(updateCounter, 1000);
