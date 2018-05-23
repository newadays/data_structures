class Node:
    def __init__(self, data=None):
        self.val = data
        self.left = None
        self.right = None


def get_node(data):
    new_node = Node(data)
    new_node.left = None
    new_node.right = None
    return new_node  # return the address of the new node


def insert_node(root, val):
    if root is None or root.val is None:
        root = get_node(val)
    elif val <= root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)
    return root


def search_node(root, data):
    if root is None or root.data is None:
        return False
    elif data == root.data:
        return True
    elif data <= root.data:
        return search_node(root.left, data)
    else:
        return search_node(root.right, data)


def find_node(root, data):
    if root is None or root.data is None:
        return root
    elif data == root.data:
        return root
    elif data <= root.data:
        return find_node(root.left, data)
    else:
        return find_node(root.right, data)


def findMin(root):
    if root is None or root.data is None:
        return root
    else:
        while root.left:
            root = root.left
        return root


def findMax(root):
    if root is None or root.data is None:
        return root

    elif root.right is None:
        return root

    return findMax(root.right)


def height(root):
    if root is None or root.data is None:
        return -1
    else:
        root.left = height(root.left)
        root.right = height(root.right)
        return max(root.left, root.right) + 1


def delete_node(root, data):
    if root is None or root.data is None:
        return root
    elif data < root.data:  # addresses of root are updated here (top of stack)
        print(root.data)
        root.left = delete_node(root.left, data)
    elif data > root.data:  # addresses of root are updated here (top of stack)
        print(root.data)
        root.right = delete_node(root.right, data)
    else:
        if root.left is None and root.right is None:
            print(root.data)
            del root
            root = None
            return root

        elif root.left is None:
            print(root.data)
            temp = root
            root = root.right
            del temp

        elif root.right is None:
            print(root.data)
            temp = root
            root = root.left
            del temp

        else:
            min_ = findMin(root.right)
            root.data = min_.data
            root.right = delete_node(root.right, min_.data)

    return root


# traversal - BFT
def bft(root):
    def bft_node(q):
        result = []
        while q:
            temp = q[-1]
            print(temp.data)
            if temp.left:
                q.insert(0, temp.left)
            if temp.right:
                q.insert(0, temp.right)
            result.append(q.pop().data)
        return result

    if root is None or root.data is None:
        return None
    else:
        que = [root]

    return bft_node(que)


# traversal DLR (PreOrder) Root -> Left -> Right
def dlr(root):
    if root is None or root.data is None:
        return None
    else:
        print(root.data)
        dlr(root.left)
        dlr(root.right)


# traversal LDR (InOrder/Binary Search Tree) Left -> Root -> Right
def ldr(root):
    if root is None or root.data is None:
        return None
    else:
        ldr(root.left)
        print(root.data)
        ldr(root.right)


# traversal LRD (PostOrder) Left -> Right -> Root
def lrd(root):
    if root is None or root.data is None:
        return None
    else:
        lrd(root.left)
        lrd(root.right)
        print(root.data)


# Check is tree is a BST - only for positive integers
def bst_check(root):
    q = []

    def bst(head):
        if head is None or head.data is None:
            return None
        else:
            bst(head.left)
            print(head.data)
            q.append(head.data)
            bst(head.right)
        return q

    if q is None:
        return False
    else:
        r = bst(root)
        return all(r[i] <= r[i + 1] for i in range(len(q) - 1))

def isValidBST(A):
    import sys
    def validate(node, minm, maxm):
        if not node:
            return 1
        return 1 if node.val > minm and node.val < maxm and validate(node.left, minm, node.val) and validate(node.right, node.val, maxm) else 0

    return validate(A, -sys.maxsize - 1, sys.maxsize)


# InOrder Successor
def inorder(root, data):
    if root is None or root.data is None:
        return None

    node = find_node(root, data)

    if node:
        if node.right is not None:  # if right subtree exists then successor is left-most (minimum) in right subtree
            return findMin(node.right).data
        else:  # find the deepest parent/ancestor for which node is in its left starting from root
            successor = None
            ancestor = root

            while node != ancestor:

                if node.data < ancestor.data:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right

            return successor.data
    else:
        return None


# @param A : root node of tree
# @param B : integer
# @return the root node in the tree
def getSuccessor(A, B):
    def findMin(A):
        head = A
        while head.left:
            head = head.left
        return head

    x = B
    root = A
    if root:
        while root.val != x:
            if x < root.val:
                root = root.left
            else:
                root = root.right

        if root.right:
            # find the leftmost node in right subtree
            return findMin(root.right)
        else:
            # find the deepest ancestor for which x is in left subtree
            ancestor = A
            successor = None
            while ancestor:
                if root.val < ancestor.val:
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = ancestor.right

            return successor
    else:
        return None


# binary tree
head = Node()  # not actually the root but a pointer to the root
# test = get_node(20)
head = insert_node(head, 15)
head = insert_node(head, 10)
head = insert_node(head, 50)
head = insert_node(head, 25)
head = insert_node(head, 7)
head = insert_node(head, 17)
head = insert_node(head, 55)
head = insert_node(head, 56)
head = insert_node(head, 13)

# unbalanced tree
# head = insert_node(head, 7)
# head = insert_node(head, 4)
# head = insert_node(head, -1)
# head = insert_node(head, 5)
# head = insert_node(head, 3)
# head = insert_node(head, -1)
# head = insert_node(head, -1)
# head = insert_node(head, -1)
# ans = search_node(head, 11)
# head = delete_node(head, 50)
# min_node = findMin(head)
# max_node = findMax(head)
# print(min_node.data)
# print(max_node.data)
# print(height(head))
# r = bft(head)
# print(r)
# print(dlr(head))
# print(ldr(head))
# print(lrd(head))
print(isValidBST(head))
# print(inorder(head, 13))


# print(head)
# print(ans)
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# case 1: node has a right subtree i.e. the min in the right subtree
# case 2: there's no right subtree - we find the deepest node


# class Solution:
#     # @param A : root node of tree
#     # @return an integer
#     def isValidBST(self, A):
#
#         # bst walktthrough and check if balanced
#         root = A
#         r_root = A
#
#         if root:
#             while root and r_root:
#                 # check left
#                 if root.left.val > root.val:
#                     return 0
#                 elif root.right.val < root.val:
#                     return 0
#                 else:
#                     root = root.left
#                 # check right
#             if r_root.left.val > r_root.val:
#                 return 0
#             elif r_root.right.val < r_root.val:
#                 return 0
#             else:
#                 r_root = r_root.right
#             return 1
#
#         else:
#             return 0
