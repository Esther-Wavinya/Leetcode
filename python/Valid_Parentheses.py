# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# To check if a string of brackets is valid, we can use a stack data structure to keep track of the opening brackets we encounter.

# 1. First, we initialize an empty stack.
# 2. Then, for each character in the string:
# 3. If the character is an opening bracket ('(', '{', '['), we push it onto the stack.
# 4. If the character is a closing bracket (')', '}', ']'), we check if the stack is empty. Ifg is valid. Otherwise, it is not valid.


class Solution:
    def isValid(self, s: str) -> bool:
        # initialize an empty stack
        stack = []
        for char in s:
            if char in ['(', '{', '[']:  # if the character is an opening bracket,
                stack.append(char)  # push it onto the stack
            else:
                if not stack:
                    return False
                # if the character is a closing bracket (')', '}', ']'),
                # we check if the stack is empty. If it is, the string is not valid.
                if char == ')' and stack[-1] == '(':
                    stack.pop()  # If it's not empty, we pop the top element from the stack and check if it matches the corresponding opening bracket. If it doesn't match, the string is not valid.
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack
