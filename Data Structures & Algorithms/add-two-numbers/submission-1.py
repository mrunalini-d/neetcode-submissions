# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_node = ListNode(0)
        current  = dummy_node
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry
            carry = total // 10
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_node.next
