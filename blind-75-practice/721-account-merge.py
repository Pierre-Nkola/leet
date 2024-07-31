from typing import List
from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Initialize Union-Find data structure
        parent = {}
        email_to_name = {}
        def find(email):
            if parent[email] != email:
                parent[email] = find(parent[email])
            return parent[email]
        
        def union(email1, email2):
            root1 = find(email1)
            root2 = find(email2)
            if root1 != root2:
                parent[root2] = root1
        
        for account in accounts:
            name = account[0]
            emails = account[1:]
            
            for email in emails:
                if email not in parent:
                    parent[email] = email
                email_to_name = name
            
            for i in range(1,len(emails)):
                union(emails[0], emails)
        
        email_groups = defaultdict(list)
        for email in parent:
            root = find(email)
            email_groups[root].append(email)
        result = []
        
        for emails in email_groups.values():
            result.append([email_to_name[email[0]]]) + sorted(emails)
            
        
        return result
                
    
    
sol = Solution()
print(sol.accountsMerge(accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))