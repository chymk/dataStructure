class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None


def PathSum(root,arr):
    if root is None:
        return
    arr.append(root.data)
    if root.left is None and root.right is None:
        print(arr," Sum :",sum(arr))
        arr.pop()
        return

    PathSum(root.left,arr)
    PathSum(root.right,arr)
    arr.pop()



if __name__== '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)

    PathSum(root,[])




