# Binary Trees - Binary Search Tree and Binary Tree
class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None


#create treenode
def getNode(x):
    node = TreeNode(x)
    return node


# insert
def insert_node(root, x):
    if root is None:
        root = getNode(x)

    elif x <= root.val:
        if root.left is None:
            root.left = getNode(x)
        else:
            insert_node(root.left, x)

    else:
        if root.right is None:
            root.right = getNode(x)
        else:
            insert_node(root.right, x)


# bft - breadth first
def bft(root):
    def bft_trav(q):
        while q:
            temp = q[-1]
            if temp.left:
                q.insert(0, temp.left)

            if temp.right:
                q.insert(0, temp.right)

            print(temp.val)
            q.pop()

    bft = bft_trav([root])


# dft - depth first search
# DRL - PreOrder : root -> left -> right
def drl(root):
    if root is None:
        return
    else:
        print(root.val)
        drl(root.left)
        drl(root.right)


# LDR - InOrder : left -> root -> right
def ldr(root):
    if root is None:
        return
    else:
        ldr(root.left)
        print(root.val)
        ldr(root.right)


# LRD - PostOrder : left -> right -> root
def lrd(root):
    if root is None:
        return
    else:
        lrd(root.left)
        lrd(root.right)
        print(root.val)


def search(root, val):
    if root is None:
        return None
    else:
        if root.val == val:
            return root
        elif val < root.val:
            return search(root.left, val)
        else:
            return search(root.right, val)


def findMin(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root


def findMax(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root


# delete a node
# case 1 - leaf node
# case 2 - node with single child - set move the parent of deleted down
# case 3 - Has both left and right child

def delete_node(root, val):
    if root is None:
        return None
    elif val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        if root.left is None and root.right is None:
            del root
            root = None
            return root
        elif root.left is None:
            temp = root
            root = root.right
            del temp
        elif root.right is None:
            temp = root
            root = root.left
            del temp
        else:
            min_ = findMin(root.right)
            root.val = min_.val
            root.right = delete_node(root.right, min_.val)
    return root


def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1

# @param A : root node of tree
# @return an integer


def minDepth(A):
    root = A
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    if root.right is None:
        return minDepth(root.left) + 1
    if root.left is None:
        return minDepth(root.right) + 1

    return min(minDepth(root.left), minDepth(root.right))+1


# Function to find LCA of n1 and n2. The function assumes
# that both n1 and n2 are present in BST
def lca(A, B, C):

    def lca_(root, n1, n2):
        if root is None:
            return None
        elif n1 < root.val and n2 < root.val:
            return lca(root.left, n1, n2)
        elif n1 > root.val and n2 > root.val:
            return lca(root.right, n1, n2)
        return root

    chk1 = search(A, B)
    chk2 = search(A, C)

    if chk1 and chk2:
        return lca_(A, B, C).val
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

def isValidBST(A):
    import sys
    def validate(node, minm, maxm):
        if not node:
            return 1
        return 1 if node.val > minm and node.val < maxm and validate(node.left, minm, node.val) and validate(node.right, node.val, maxm) else 0

    return validate(A, -sys.maxsize - 1, sys.maxsize)

head = TreeNode(10)
insert_node(head, 5)
insert_node(head, 7)
insert_node(head, 2)
insert_node(head, 15)
insert_node(head, 25)
insert_node(head, 11)
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

# bft(head)
# drl(head)
# ldr(head)
# lrd(head)
# print(search(head, 11))
# print(findMin(head).val)
# print(height(head))
# print(lca(head, 5, 11).val)
# drl(head)


# Finds the path from root node to given root of the tree.
# Stores the path in a list path[], returns true if path
# exists otherwise false
# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(head, n1, n2):
    # Code here
    p1 = []
    p2 = []

    def path(root, ls, n):
        if root is None:
            return False

        ls.append(root.val)

        if root.val == n:
            return True

        if (root.left != None and path(root.left, ls, n) != False) or (
                root.right != None and path(root.right, ls, n) != False):
            return True
        ls.pop()
        return False

    path(head, p1, n1)
    path(head, p2, n2)

    if n1 in p1 and n2 in p2:
        i = 0
        while (i < (len(p1) - 1)) and (i < (len(p1) - 1)):
            if p1[i] != p2[i]:
                break
            i += 1
        return p1[i - 1]
    else:
        return -1


# print(findLCA(head, 5, 11))


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    ls = []

    def __init__(self, root):
        st = []
        self.ls = self.ldr(root, st)

    def ldr(self, root, st):
        if root is None:
            return
        else:
            self.ldr(root.left, st)
            st.insert(0, root.val)
            self.ldr(root.right, st)
        return st

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return True if self.ls else False

    # @return an integer, the next smallest number
    def next(self):
        return self.ls.pop()


# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),



test = BSTIterator(head)
print(test.ls)
print(test.next())
print(test.next())


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert_node(root, val):
    if root is None or root.val is None:
        root = getNode(val)
    else:
        if val <= root.val:
            if root.left is None:
                root.left = getNode(val)
            else:
                root.left = insert_node(root.left, val)
        else:
            if root.right is None:
                root.right = getNode(val)
            else:
                root.right = insert_node(root.right, val)
    return root


def traverse(root):
    if root is None or root.val is None:
        return

    traverse(root.left)
    print(root.val)
    traverse(root.right)


tree = TreeNode(None)
tree = insert_node(tree, 15)
tree = insert_node(tree, 10)
tree = insert_node(tree, 50)
tree = insert_node(tree, 7)
tree = insert_node(tree, 13)
tree = insert_node(tree, 25)
tree = insert_node(tree, 17)
tree = insert_node(tree, 55)
tree = insert_node(tree, 56)
traverse(tree)


