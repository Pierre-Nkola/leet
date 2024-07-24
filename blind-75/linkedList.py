class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
        

class LinkedListMethods: 
    def  buildLinkedList(self, nums: list):
        dummy = ListNode()
        curr = dummy
        for num in nums:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next
    
    def printLinkedList(self, head: ListNode):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")