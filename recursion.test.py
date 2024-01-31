import unittest

from recursion import (
    product,
    longest,
    everyOther,
    isPalindrome,
    findIndex,
    revString,
    gatherStrings,
    binarySearch
)

class TestRecursionFunctions(unittest.TestCase):

    def test_product(self):
        self.assertEqual(product([2, 3, 4]), 24)
        self.assertEqual(product([1, -1, 1, -1, 1, -1]), -1)
        self.assertEqual(product([10]), 10)

    def test_longest(self):
        self.assertEqual(longest(["hello", "hi", "hola"]), 5)
        self.assertEqual(longest(["abcdefg", "hijklmnop", "qrs", "tuv", "wx", "y", "z"]), 9)
        self.assertEqual(longest(["a", "b", "c", "d", "e"]), 1)
        self.assertEqual(longest(["abcde"]), 5)

    def test_everyOther(self):
        self.assertEqual(everyOther("hello"), "hlo")
        self.assertEqual(everyOther("banana stand"), "bnn tn")
        self.assertEqual(everyOther("ddoouubbllee"), "double")
        self.assertEqual(everyOther("hi"), "h")
        self.assertEqual(everyOther("z"), "z")

    def test_isPalindrome(self):
        self.assertTrue(isPalindrome("tacocat"))
        self.assertTrue(isPalindrome("racecar"))
        self.assertTrue(isPalindrome("a"))
        self.assertTrue(isPalindrome("helloolleh"))
        self.assertFalse(isPalindrome("tacodog"))
        self.assertFalse(isPalindrome("az"))
        self.assertFalse(isPalindrome("goodbye"))

    def test_findIndex(self):
        animals = ["duck", "cat", "pony", "cat"]
        self.assertEqual(findIndex(animals, "duck"), 0)
        self.assertEqual(findIndex(animals, "cat"), 1)
        self.assertEqual(findIndex(animals, "pony"), 2)
        self.assertEqual(findIndex(animals, "porcupine"), -1)
        self.assertEqual(findIndex(animals, "turtle"), -1)

    def test_revString(self):
        self.assertEqual(revString("porcupine"), "enipucrop")
        self.assertEqual(revString("duck"), "kcud")
        self.assertEqual(revString("cat"), "tac")
        self.assertEqual(revString("pony"), "ynop")

    def test_gatherStrings(self):
        whiskey = {
            "name": "Whiskey",
            "age": 5,
            "favFood": "popcorn",
            "color": "black",
            "barks": False
        }
        self.assertEqual(sorted(gatherStrings(whiskey)), sorted(["Whiskey", "popcorn", "black"]))
        
        nestedObj = {
            "firstName": "Lester",
            "favoriteNumber": 22,
            "moreData": {
                "lastName": "Testowitz"
            },
            "funFacts": {
                "moreStuff": {
                    "anotherNumber": 100,
                    "deeplyNestedString": {
                        "almostThere": {
                            "success": "you made it!"
                        }
                    }
                },
                "favoriteString": "nice!"
            }
        }
        self.assertEqual(sorted(gatherStrings(nestedObj)), sorted(["Lester", "Testowitz", "you made it!", "nice!"]))

    def test_binarySearch(self):
        self.assertEqual(binarySearch([1, 2, 3, 4], 4), 3)
        self.assertEqual(binarySearch([1, 2], 1), 0)
        self.assertEqual(binarySearch([1, 2, 3, 4, 5, 6, 7], 6), 5)
        self.assertEqual(binarySearch([1, 2, 3, 4], 0), -1)
        self.assertEqual(binarySearch([1, 2], 11), -1)

if __name__ == '__main__':
    unittest.main()