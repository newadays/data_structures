#   You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8

#  342 + 465 = 807
# Make sure there are no trailing zeros in the output list
# So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.

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

    def get_k(self, k):
        current_node = self.head
        i = 1

        while current_node:
            if i == k:
                return current_node.data
            current_node = current_node.get_next()
            i += 1

        if current_node is None:
            raise ValueError("k is longer than list")


A = LinkedList()
a = [2, 3, 5, 1, 8, 2, 3, 3, 1]

for i in a:
    A.insert(i)

# print(A.search(5))
# print(A.size())

# print(A.removeDups())
# print(A.size())
# print(A.get_k(4))
B = LinkedList()
b = [2, 3, 5, 1, 8, 2, 3, 3, 10]

for i in b:
    B.insert(i)


def sum_ll(A, B):
    n = A.size()
    m = B.size()
    R = LinkedList()
    a = ''
    b = ''
    # case 1
    if n == m:
        i = n
        while i > 0:
            a += str(A.get_k(i))
            b += str(B.get_k(i))
            i -= 1
        print(a)
        print(b)
        s = int(a) + int(b)
        s = str(s)
        for i in s:
            R.insert(int(i))
        return R

    else:
        # case 2
        if n > m:
            d = n - m
            # add zeros to first of A
            i = m
            while i > d:
                a += str(A.get_k(i))
                b += str(B.get_k(i))
                i -= 1

            i = d
            a_rem = []
            while i > 0:
                a_rem+=str(A.get_k(i))
                i-=1

            a += a_rem
            s = str(int(a) + int(b))

            for i in s:
                R.insert(int(i))
            return R
        # case 3
        else:
            d = m - n
            # add zeros to first of A
            i = n
            while i > d:
                a += str(A.get_k(i))
                b += str(B.get_k(i))
                i -= 1

            i = d
            b_rem = ''
            while i > 0:
                b_rem+=str(B.get_k(i))
                i-=1

            b += b_rem
            s = str(int(a) + int(b))
            for i in s:
                R.insert(int(i))
            return R


r = sum_ll(A, B)

print(r.size())
