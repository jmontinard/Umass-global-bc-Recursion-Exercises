/** product: calculate the product of an array of numbers. */
function product(nums) {
  return nums.reduce((acc, num) => acc * num, 1);
}

/** longest: return the length of the longest word in an array of words. */
function longest(words) {
  return Math.max(...words.map(word => word.length));
}

/** everyOther: return a string with every other letter. */
function everyOther(str) {
  return str.split('').filter((_, idx) => idx % 2 === 0).join('');
}

/** isPalindrome: checks whether a string is a palindrome or not. */
function isPalindrome(str) {
  const cleanStr = str.replace(/[\W_]/g, '').toLowerCase();
  return cleanStr === cleanStr.split('').reverse().join('');
}

/** findIndex: return the index of val in arr (or -1 if val is not present). */
function findIndex(arr, val) {
  return arr.indexOf(val);
}

/** revString: return a copy of a string, but in reverse. */
function revString(str) {
  return str.split('').reverse().join('');
}

/** gatherStrings: given an object, return an array of all of the string values. */
function gatherStrings(obj) {
  let stringsArray = [];
  for (let key in obj) {
    if (typeof obj[key] === 'string') {
      stringsArray.push(obj[key]);
    } else if (typeof obj[key] === 'object' && !Array.isArray(obj[key]) && obj[key] !== null) {
      stringsArray = stringsArray.concat(gatherStrings(obj[key]));
    }
  }
  return stringsArray;
}

/** binarySearch: given a sorted array of numbers, and a value,
 * return the index of that value (or -1 if val is not present). */
function binarySearch(arr, val) {
  let left = 0;
  let right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (arr[mid] === val) {
      return mid;
    } else if (arr[mid] < val) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

module.exports = {
  product,
  longest,
  everyOther,
  isPalindrome,
  findIndex,
  revString,
  gatherStrings,
  binarySearch
};