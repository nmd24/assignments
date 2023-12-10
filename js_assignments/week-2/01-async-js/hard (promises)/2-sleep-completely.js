/*
 * Write a function that halts the JS thread (make it busy wait) for a given number of milliseconds.
 * During this time the thread should not be able to do anything else.
 */

function sleep(milliseconds) {
    const start = new Date().getTime();
    let end = start;
    while (end - start < milliseconds) {
        end = new Date().getTime();
    }
}

// Usage example
console.log("Sleeping for 5 seconds...");
sleep(5000); // Sleep for 3000 milliseconds
console.log("Woke up!");