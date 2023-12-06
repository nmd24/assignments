/*
  Implement a function `countVowels` that takes a string as an argument and returns the number of vowels in the string.
  Note: Consider both uppercase and lowercase vowels ('a', 'e', 'i', 'o', 'u').

  Once you've implemented the logic, test your code by running
*/

function countVowels(str) {
  // Define the vowels
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  // Convert the string to lowercase to make the function case-insensitive
  str = str.toLowerCase();

  // Initialize a counter for vowels
  let vowelCount = 0;

  // Iterate over each character in the string
  for (let char of str) {
      // If the character is a vowel, increment the counter
      if (vowels.includes(char)) {
          vowelCount++;
      }
  }

  // Return the total count of vowels
  return vowelCount;
}

module.exports = countVowels;