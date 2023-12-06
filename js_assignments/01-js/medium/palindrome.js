/*
  Implement a function `isPalindrome` which takes a string as argument and returns true/false as its result.
  Note: the input string is case-insensitive which means 'Nan' is a palindrom as 'N' and 'n' are considered case-insensitive.
*/

function isPalindrome(str) {
  // Remove non-letter characters and convert to lowercase
  const cleanedStr = str.replace(/[^A-Za-z]/g, '').toLowerCase();

  // Compare the cleaned string with its reverse
  return cleanedStr === cleanedStr.split('').reverse().join('');
}

module.exports = isPalindrome;
