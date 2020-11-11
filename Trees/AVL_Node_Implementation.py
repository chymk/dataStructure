class AVLNode:
    def __init__(self,data,balanceFactor,left,right):
        self.data = data
        self.balanceFactor = 0
        self.left = left
        self.right = right

class AVLTree:
    def __init__(self):
        self.root = None

    def inOrderPrint(self):
        self.recInOrder(self.root)

    def recInOrderPrint(self,root):
        if root:
            self.recInOrderPrint(root.left)
            print(root.data,end=" ")
            self.recInOrderPrint(root.right)

    def insert(self,data):
        newNode = AVLNode(data,0,None,None)
        [self.root,taller] = self.recInsertAVL(self.root,newNode)

    def recInsertAVL(self,root,newNode):
        if root is None:
            root = newNode
            root.balanceFactor = 0
            taller = True
        elif newNode.data<root.data:
            [root.left,taller] = self.recInsertAVL(root.left,newNode)
            if taller:
                if root.balanceFactor == 0:
                    root.balanceFactor = -1
                elif root.balanceFactor == 1:
                    root.balanceFactor = 0
                else:
                    root = self.rightLeftRotate(root)
                    taller = False
        else:
            [root.right,taller] = self.recInsertAVL(root.right,newNode)
            if taller:
                if root.balanceFactor == -1:
                    root.balanceFactor = 0
                elif root.balanceFactor == 0:
                    root.balanceFacor = 1
                else:
                    root = self.rightLeftRotate(root)
                    taller = False
        return [root,taller]

    def rightLeftRotate(self,root):
        X = root.right
        if X.balanceFactor == 1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.singleRightRotate(root)
        else:
            Y=X.left
            if Y.balanceFactor == -1:
                root.balanceFactor = 0
                X.balanceFactor = 1
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor - -1
                X.balanceFactor = 0
            Y.balanceFactor = 0
            root.right = self.sigleLeftRotate(X)
            root = self.singleRightRotate(root)
        return root

    def rightLeftRotate(self,root):
        X = root.left
        if X.balanceFactor == -1:
            root.balanceFactor = 0
            X.balanceFactor = 0
            root = self.sigleLeftRotate(root)
        else:
            Y = X.right
            if Y.balanceFactor == -1:
                root.balanceFactor = 1
                X.balanceFactor = 0
            elif Y.balanceFactor == 0:
                root.balanceFactor = 0
                X.balanceFactor = 0
            else:
                root.balanceFactor = 0
                X.balanceFactor = -1
            Y.balanceFactor = 0
            root.left = self.sigleRightRotate(X)
            root = self.singleLeftRotate(root)
        return root

    def singleRightRotate(self,root):
        X = root.right
        root.right = X.left
        X.left = root
        return X

    def singleLeftRotate(self,root):
        X = root.left
        root.left = X.right
        X.right = root
        return X

    def height(self):
        return self.recHeight(self.root)

    def recHeight(self,root):
        if root == None:
            return 0
        else:
            return max(self.recHeight(root.left),self.recHeight(root.right))+1

def tester():
    avl = AVLTree()
    data = [3,1,9,6,0,11,2,5,4]

    for i in range(len(data)):
        avl.insert(data[i])
    avl.inOrderPrint()
    print("height = ",avl.height())

if __name__ == "__main__":
    tester()


