

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def get_node(data):
    new_node = Node(data)
    new_node.left = None
    new_node.right = None
    return new_node  # return the address of the new node


def insert_node(root, data):
    if root is None or root.data is None:
        root = get_node(data)
    elif data <= root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
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
    elif data < root.data:   # addresses of root are updated here (top of stack)
        print(root.data)
        root.left = delete_node(root.left, data)
    elif data > root.data:   # addresses of root are updated here (top of stack)
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
    if root is None or root.data  is None:
        return None
    else:
        lrd(root.left)
        lrd(root.right)
        print(root.data)




# binary tree
head = Node()    # not actually the root but a pointer to the root
# test = get_node(20)
head = insert_node(head, 15)
head = insert_node(head, 10)
head = insert_node(head, 50)
head = insert_node(head, 25)
head = insert_node(head, 7)
head = insert_node(head, 17)
head = insert_node(head, 55)
head = insert_node(head, 56)

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
print(lrd(head))
print(head)
# print(ans)
