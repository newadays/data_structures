#  You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#  342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

# Definition for singly-linked list.


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    def get_node(self, k):
        current = self.next
        i = 0
        while i < k:
            current = current.next
            i += 1
        return current

    def insert_node(self, val):
        new_node = Node(val)
        new_node.next = self.next
        self.next = new_node

    def delete_node(self, val):
        if self.next.val == val:
            self.next = self.next.next
        else:
            curr = self.next
            while curr:
                if curr.next and curr.next.val == val:
                    curr.next = curr.next.next
                curr = curr.next

    def insert_kth_node(self, k, val):
        curr = self.next
        prev = None
        i = 1
        while curr:

            if i == k:
                new_node = Node(val)
                prev.next = new_node
                new_node.next = curr
                break
            i += 1
            prev = curr
            curr = curr.next

    def delete_kth_node(self, k):
        if k > 0 and self:
            if k == 1:
                # head node
                self.next = self.next.next
            else:
                curr = self.next
                i = 1
                # delete head to be handled later
                while curr:
                    i += 1

                    if i == k:
                        curr.next = curr.next.next

                    curr = curr.next

    def reverse(self):
        prev = None
        curr = self.next

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.next = prev

    def reverseBtw(self, m, n):
        # case 1
        # LL btw m and n
        # case 2
        # LL ==n(head) but m less than tail
        # LL n shorter than (head) but m == tail
        # @param A : head node of linked list
        # @param B : integer
        # @param C : integer
        # @return the head node in the linked

        def reversemn(curr_node, i, j):
            next = None
            tail_node = None
            prev_node = None
            while i <= j and curr_node:
                i += 1
                next = curr_node.next
                curr_node.next = prev_node
                if tail_node is None:
                    tail_node = curr_node

                prev_node = curr_node
                curr_node = next

            return prev_node, tail_node, curr_node

        k = 1
        prev = None
        curr = self.next
        while k < m and curr:
            prev = curr
            curr = curr.next
            k += 1

        start, end, after = reversemn(curr, k, n)

        if end:
            end.next = after

        if prev:
            prev.next = start
        else:
            self.next = start

        def deleteDuplicates(self, A):
            head = A
            while A:
                while A.next and A.next.val == A.val:
                    A.next = A.next.next
                A = A.next
            return head


head = Node()

head.insert_node(11)
head.insert_node(12)
head.insert_node(31)
head.insert_node(41)
head.insert_node(51)

# head.delete_node(4)

head.insert_kth_node(2, 32)

# head.delete_kth_node(1)
curr = head.next

while curr:
    print(curr.val)
    curr = curr.next

head.reverseBtw(2, 4)

curr = head.next

while curr:
    print(curr.val)
    curr = curr.next


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
# @param B : head node of linked list
# @return the head node in the linked list
def getIntersectionNode(A, B):
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


# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    curr = head
    size = 0
    while curr != None:
        size += 1
        curr = curr.next

    # only one node
    if size == 1:
        head = None
        return head
    if size <= n:
        head = head.next
        return head

    s = size - n + 1
    curr = head
    for i in range(0, s - 2):
        curr = curr.next

    curr.next = curr.next.next
    return head


# Palindromes
# @param A : head node of linked list
# @return an integer
def lPalin_(A):
    # find len, reverse half and compare

    if A:
        if A.next:
            l = []
            s = []
            while A:
                l.append(A.val)
                s.insert(0, A.val)
                A = A.next

            while l:
                if l.pop() != s.pop():
                    return 0
        return 1
    else:
        return 0


def lPalin(A):
    reverse = None
    slow = fast = A
    while fast and fast.next:
        fast = fast.next.next
        # Reverse the first half
        reverse, reverse.next, slow = slow, reverse, slow.next
    # If list has odd no. of nodes
    if fast:
        slow = slow.next
    # Expand from the mid node
    while reverse and reverse.val == slow.val:
        slow = slow.next
        reverse = reverse.next
    return int(not reverse)


# @param A : head node of linked list
# @return the first node in the cycle in the linked list
def detectCycle(A):
    ls = {}
    if A is not None and A.val is not None:
        while A.next:
            if hash(A.val) in ls:
                return ls[A.val]
            else:
                ls[A.val] = A
            A = A.next
        return None
    else:
        return None


# root = removeNthFromEnd(root, 1)
# root = lPalin(root)

