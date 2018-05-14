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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked
    def reverseBetween(self, A, B, C):

        def size(A):
            current_node = A.head
            count = 0
            while current_node:
                count += 1
                current_node = current_node.next()
            return count

        def get_node(A, k):
            current_node = A.head
            i = 1
            while current_node:
                if i == k:
                    return current_node
                current_node = current_node.next()
                i += 1

        def reverse(A):
            current_node = A.head
            prev_node = None
            while current_node:
                next = current_node.next_node
                current_node.next = prev_node
                prev_node = current_node
                current_node = next

            A.head = prev_node
            return A

        n = C
        m = B
        n_node = get_node(A, n)
        if m > 1:
            prev_node = get_node(A, m - 1)
            m_node = get_node(A, m)
            current_node = m_node
            while current_node.next_node == n_node:
                next = current_node.next_node
                current_node.next_node = prev_node
                prev_node = current_node
                current_node = next

            if size(A) == n:
                A.head = prev_node
        else:
            reverse(A)

        return A

#LinkedList Class
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.get_next()
        return count

    def search(self, data):
        current_node = self.head
        found = False
        while current_node and found is False:
            if current_node.data == data:
                found = True
            current_node = current_node.get_next()

        if current_node is None and found is False:
            raise ValueError("not found")

        return current_node

    def delete(self, data):
        current_node = self.head
        previous_node = None
        found = False
        while current_node and found is False:
            if current_node.data == data:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()

        if current_node is None and found is False:
            raise ValueError("not found")

        if previous_node is None:
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.next_node)

    def removeDups(self):
        l = []
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.data in l:
                previous_node.set_next(current_node.next_node)
                current_node = current_node.get_next()
            else:
                l.append(current_node.data)

                previous_node = current_node
                current_node = current_node.get_next()