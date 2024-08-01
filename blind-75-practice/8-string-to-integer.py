class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        # Initialize variables
        sign = 1
        res = 0
        index = 0
        n = len(s)
        
        # Check for sign
        if index < n and s[index] in ['+', '-']:
            sign = -1 if s[index] == '-' else 1
            index += 1
        
        # Convert digits to integer
        while index < n and s[index].isdigit():
            res = res * 10 + int(s[index])
            index += 1
        
        # Apply sign and clamp to 32-bit signed integer range
        res *= sign
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
        
        return res
