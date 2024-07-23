from typing import Optional
from linkedList import LinkedListMethods

class ListNode:
    def __init__(self, val =0, next = None) -> None:
        self.val = val 
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1:Optional[ListNode], list2: Optional[ListNode])-> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
                
            curr = curr.next
            
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        
        return dummy.next
    
sol = Solution()
linkedLists = LinkedListMethods()


list1 = linkedLists.buildLinkedList([1, 2, 4])
list2 = linkedLists.buildLinkedList([1,3,4])
printedList1 = linkedLists.printLinkedList(list1)
printedLists = linkedLists.printLinkedList(list2)

merged_lists = sol.mergeTwoLists(list1,list2)
linkedLists.printLinkedList(merged_lists)