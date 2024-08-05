class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        # Dictionary to count characters in t
        t_count, window = {}, {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        res, resLen = [-1, -1], float("infinity")
        have, need = 0, len(t_count)
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in t_count and window[c] == t_count[c]:
                have += 1
            
            while have == need:
                # Update result if the current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Try to contract the window
                window[s[l]] -= 1
                if s[l] in t_count and window[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

# Example usage
sol = Solution()
print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))  # Output: "BANC"
