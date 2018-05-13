#   You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#  342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    
    
    def addTwoNumbers(self, A, B):
        head = ListNode(0)
        pointer = head
        carry_over = 0
        while A and B:
            s = A.val + B.val + carry_over
            pointer.next = ListNode(s % 10)
            pointer = pointer.next
            carry_over = int(s/10)
            A = A.next
            B = B.next
        
        if A is None:
            while B:
                s = B.val + carry_over
                pointer.next = ListNode(s % 10)
                pointer = pointer.next
                carry_over = int(s/10)
                B = B.next
        
        if B is None:
            while A:
                s = A.val + carry_over
                pointer.next = ListNode(s % 10)
                pointer = pointer.next
                carry_over = int(s/10)
                A = A.next
                
        if carry_over > 0:
            pointer.next = ListNode(carry_over)
        
        return head.next
