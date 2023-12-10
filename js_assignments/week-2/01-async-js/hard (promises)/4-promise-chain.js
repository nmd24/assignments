/*
 * Write 3 different functions that return promises that resolve after 1, 2, and 3 seconds respectively.
 * Write a function that sequentially calls all 3 of these functions in order.
 * Print out the time it takes to complete the entire operation.
 * Compare it with the results from 3-promise-all.js
 */
function waitOneSecond() {
    return new Promise(resolve => setTimeout(resolve, 1000));
}

function waitTwoSeconds() {
    return new Promise(resolve => setTimeout(resolve, 2000));
}

function waitThreeSeconds() {
    return new Promise(resolve => setTimeout(resolve, 3000));
}

function calculateTime() {
    const startTime = new Date();

    waitOneSecond()
        .then(() => {
            console.log("Finished 1 second wait");
            return waitTwoSeconds();
        })
        .then(() => {
            console.log("Finished 2 seconds wait");
            return waitThreeSeconds();
        })
        .then(() => {
            console.log("Finished 3 seconds wait");
            const endTime = new Date();
            const timeTaken = endTime - startTime;
            console.log(`Total time taken: ${timeTaken} milliseconds`);
        });
}

calculateTime();