from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
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
new_head = sol.reverseList(head)

# Print the result: 2 -> 1 -> 4 -> 3
printList(new_head)

