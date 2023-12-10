let counter = 0; // Counter to track seconds since script started

// Function to format time into 24-hour format
function formatTime24H(date) {
    let hours = String(date.getHours()).padStart(2, '0');
    let minutes = String(date.getMinutes()).padStart(2, '0');
    let seconds = String(date.getSeconds()).padStart(2, '0');
    return `${hours}:${minutes}:${seconds}`;
}

// Function to format time into 12-hour format
function formatTime12H(date) {
    let hours = date.getHours();
    let minutes = String(date.getMinutes()).padStart(2, '0');
    let seconds = String(date.getSeconds()).padStart(2, '0');
    let ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? String(hours).padStart(2, '0') : '12'; // the hour '0' should be '12'
    return `${hours}:${minutes}:${seconds} ${ampm}`;
}

// Function to update the clock
function updateClock() {
    let now = new Date();
    console.log("24-Hour Format:", formatTime24H(now));
    console.log("12-Hour Format:", formatTime12H(now));
    counter += 1;
}

// Set interval to call updateClock function every 1000 milliseconds (1 second)
setInterval(updateClock, 1000);
