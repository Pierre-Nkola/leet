# Given a linked list, swap every two adjacent nodes a
# nd return its head. You must solve the problem without 
# modifying the values in the list's nodes (i.e., only nodes 
# themselves may be changed.)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        first = head
        second = head.next
        
        first.next = self.swapPairs(second.next)
        second.next = first
        
        return second
    
def printList(head: Optional[ListNode]) -> None:
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

# Example usage
sol = Solution()

# Create a linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Swap pairs
new_head = sol.swapPairs(head)

# Print the result: 2 -> 1 -> 4 -> 3
printList(new_head)