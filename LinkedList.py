# #   You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# # Output: 7 -> 0 -> 8
#
# #  342 + 465 = 807
# # Make sure there are no trailing zeros in the output list
# # So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
#
# # Definition for singly-linked list.


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

    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked
    def reverseBetween(self, head, m, n):
        def reverse(head, m, n):
            c = m
            tail = None
            prev, curr = None, head
            while c <= n and curr:
                c += 1
                temp = curr.next
                curr.next = prev
                if tail is None:
                    tail = curr
                prev = curr
                curr = temp
            return prev, tail, curr

        if not head or not head.next:
            return head

        c = 1
        prev, curr = None, head
        while c < m and curr:
            c += 1
            prev, curr = curr, curr.next

        start, end, after = reverse(curr, c, n)
        if end:
            end.next = after
        if prev:
            prev.next = start
        else:
            head = start
        return head

    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def getIntersectionNode(self, A, B):
        def length(A):
            current_node = A
            count = 1
            while current_node:
                count += 1
                current_node = current_node.next
            return count

        m = length(A)
        n = length(B)
        if m > 0 and n > 0:
            d = abs(m - n)

            i = 0
            if d != 0:
                if m > n:
                    while i < d:
                        A = A
                        A = A.next
                        i += 1
                else:
                    while i < d:
                        B = B
                        B = B.next
                        i += 1

            while A and B:
                if (A == B):
                    return A
                else:
                    A = A.next
                    B = B.next

        return None

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
#
#

class ListNodes:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_node(self, k):
        current = self.next
        i = 0
        while i < k:
            current = current.next
            i += 1
        return current

    def insert_node(self, data):
        node = ListNode(data)
        node.next = self.next
        self.next = node


a = [2,3,4,5,10]
A = ListNodes(None)

for i in a:
    A.insert_node(i)

second_node = A.get_node(2)
print(second_node)
print(A)