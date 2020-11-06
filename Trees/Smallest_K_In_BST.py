class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return Node(key)
    if root.data == key:
        return root
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)

count = 0
def smallestKthElementBST(root,k):
    global count
    if root:
        smallestKthElementBST(root.left, k)
        count += 1
        if k == count:
            print(root.data)
            exit(1)
            return root.data
        smallestKthElementBST(root.right, k)



r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

printInorder(r)
print("")
print(smallestKthElementBST(r,3).data)


