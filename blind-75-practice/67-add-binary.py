class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass
        
        a, b = a[::-1], b[::-1]
        carry = 0
        res = ""
        
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            
            total = digitA + digitB + carry
            digit = str(total % 2)
            carry = total // 2
            
            res = digit + res
            
        if carry:
            res = str(carry) + res
            
        return res