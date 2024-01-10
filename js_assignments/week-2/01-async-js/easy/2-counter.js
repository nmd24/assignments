let counter = 0; // Starting point of the counter

// Function to update the counter
function updateCounter() {
    counter += 1;
    console.log(counter);
    // Recursively call updateCounter after 1 second
    setTimeout(updateCounter, 1000);
}
// Initial call to start the process
updateCounter();
