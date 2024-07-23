class Solution:
    def isValid(s:str):
        s = ''.join([char for char in s if char.isalnum()]).lower()
        
        l,r = 0, len(s) -1
        
        if s == '':
            return True
        
        while r > l:
            if s[r] != s[r]:
                return False
            else:
                r -= 1
                l += 1
        return True