# can't do recursion without going throu fibonacci
# let's add memiozation into it

class Solution:
    def fib(self, n):
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
    def fibMem(self, n):
        cache = {}
        def fibRecur(n):
            if n in cache:
                return cache[n]
            
            if n < 2:
                return n
            
            else:
                res = fibRecur(n-1) + fibRecur(n-2)
            
            cache[n] = res
            
            return res
        return fibRecur(n)
        
        
sol = Solution()
print(sol.fibMem(4))