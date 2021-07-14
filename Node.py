class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self.left = self.right = None

    def __str__(self):
        return str(self.key)

    def preorder(self):
        if self != None:
            print(self.key)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self != None:
            if self.left:
                self.left.preorder()
            print(self.key)
            if self.right:
                self.right.preorder()
    
    def postorder(self):
        if self != None:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
            print(self.key)