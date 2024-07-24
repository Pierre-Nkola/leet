# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head and not head.next:
            return False
        
        slow, fast = head, head,next
        
        while fast and fast.next:
            if fast == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next 
        return False