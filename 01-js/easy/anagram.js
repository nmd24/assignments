/*
  Write a function `isAnagram` which takes 2 parameters and returns true/false if those are anagrams or not.
  What's Anagram?
  - A word, phrase, or name formed by rearranging the letters of another, such as spar, formed from rasp.
*/

function isAnagram(str1, str2) {
  // Check for equal length of original strings (including non-alphabetic characters)
  if (str1.length !== str2.length) {
      return false;
  }

  // Normalize the strings: remove non-letter characters and convert to lowercase
  const normalizeString = (str) => str.replace(/[^\w]/g, '').toLowerCase();

  str1 = normalizeString(str1);
  str2 = normalizeString(str2);

  // Count letter frequencies
  const charCount = (str) => {
      const count = {};
      for (let char of str) {
          count[char] = (count[char] || 0) + 1;
      }
      return count;
  };

  const str1CharCount = charCount(str1);
  const str2CharCount = charCount(str2);

  // Compare letter frequencies
  for (let char in str1CharCount) {
      if (str1CharCount[char] !== str2CharCount[char]) {
          return false;
      }
  }

  return true;
}

module.exports = isAnagram;