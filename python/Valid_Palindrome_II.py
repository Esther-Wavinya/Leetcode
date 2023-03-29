# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# Example 1:
# Input: s = "aba"
# Output: true


# Example 2:
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.


# Example 3:
# Input: s = "abc"
# Output: false

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.

# To solve this problem, we can use a two-pointer approach where we compare the characters at the beginning and end of the string. If they are the same, we move both pointers towards the center. If they are different, we check if deleting either the left or right character results in a palindrome. If it does, we return True, otherwise, we return False.
class Solution:
    # valindrome function takes a string s as input and returns a boolean
    def validPalindrome(self, s: str) -> bool:
        laft, right = 0, len(s) - 1  # initializing two pointers left and right
        while left < right:  # iterating through the string comparing the characters left and right
            if s[left] != s[right]:  # if they are not the same,
                # check whether deleting either the left or right character results in a palindrome by calling the isPalindrome function.
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1  # if deleting either character results in a palindrome,
            right += 1  # if deleting either character results in a palindrome,
        return True  # the function returns True, otherwise, the function returns false

    # the isPalindrome function takes a string s, a left index left and a right index right as input and returns a boolean value indicating whether the string is a palindrome between the given indices.
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        # iterate through the string comparing the characters at left and right.
        while left < right:
            if s[left] != s[right]:  # if they are not the same, the function returns False
                return False
            left += 1  # Otherwise, it continues iterating until left and right meet in the middle of the string
            right += 1  # Otherwise, it continues iterating until left and right meet in the middle of the string
        # if the function has not returned False before reaching the middle, it returns True.
        return True


# The validPalindrome function takes a string s as input and returns a boolean value indicating whether the string can be palindrome after deleting at most one character from it. The function first initializes two pointers left and right at the beginning and end of the string, respectively. Then, it iterates through the string comparing the characters at left and right. If they are not the same, it checks whether deleting either the left or right character results in a palindrome by calling the isPalindrome function. If deleting either character results in a palindrome, the function returns True. Otherwise, the function returns False.

# The isPalindrome function takes a string s, a left index left, and a right index right as input and returns a boolean value indicating whether the string is a palindrome between the given indices. The function iterates through the string comparing the characters at left and right. If they are not the same, the function returns False. Otherwise, it continues iterating until left and right meet in the middle of the string. If the function has not returned False before reaching the middle, it returns True.
