# product: calculate the product of an array of numbers.
def product(nums):
    result = 1
    for num in nums:
        result *= num
    return result

# longest: return the length of the longest word in an array of words.
def longest(words):
    return max(len(word) for word in words)

# everyOther: return a string with every other letter.
def everyOther(string):
    return string[::2]

# isPalindrome: checks whether a string is a palindrome or not.
def isPalindrome(string):
    clean_str = ''.join(filter(str.isalnum, string)).lower()
    return clean_str == clean_str[::-1]

# findIndex: return the index of val in arr (or -1 if val is not present).
def findIndex(arr, val):
    try:
        return arr.index(val)
    except ValueError:
        return -1

# revString: return a copy of a string, but in reverse.
def revString(string):
    return string[::-1]

# gatherStrings: given an object, return an array of all of the string values.
def gatherStrings(obj):
    strings_list = []
    for key, value in obj.items():
        if isinstance(value, str):
            strings_list.append(value)
        elif isinstance(value, dict):
            strings_list.extend(gatherStrings(value))
    return strings_list

# binarySearch: given a sorted array of numbers, and a value,
# return the index of that value (or -1 if val is not present).
def binarySearch(arr, val):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return -1