# A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

#     For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.


# Example 1:
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


# Constraints:
#     1 <= s.length <= 20
#     s consists of digits only.


# To solve this problem, we can use a recursive approach. We can start by placing a dot after the first integer,then after the second integer and so on until we have placed three dots. At each step, we check if the current substring forms a valid integer between 0 and 255. If it does, we continue with the next step, otherwise we backtrack
# We can keep track of the current IP address being formed and the number of dots placed so far. If we have three dots and the remaining substring forms a valid integer, we add the current IP address to the list of valid IP addresses
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []

        def backtrack(start: int, dots: int, ip: str) -> None:
            if dots == 3:
                if start < len(s) and self.is_valid(s[start:]):
                    ip += s[start:]
                    ips.append(ip)
                    return
            for i in range(start, min(start+3, len(s))):
                if self.is_valid(s[start:i+1]):
                    backtrack(i+1, dots+1, ip+s[start:i+1]+".")

        backtrack(0, 0, "")
        return ips

    def is_valid(self, s: str) -> bool:
        if len(s) == 0 or len(s) > 3:
            return False
        if s[0] == "0" and len(s) > 1:
            return False
        return int(s) <= 255
