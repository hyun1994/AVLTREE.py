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
                self.right.preorde()

    def inorder(self):
        if self != None:
            if self.left:
                self.left.preorder()
            print(self.key)
            if self.right:
                self.right.preorde()
    
    def postorder(self):
        if self != None:
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorde()
            print(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__init__()

    def height(self):
        math.abs(Node.self.left - Node.self.right) <= 1
        return height

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
            return p
    
    def search(self, key):
        v = self.find_loc(key)
        if v == None:
            return None
        else:
            return v

