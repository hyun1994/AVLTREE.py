from Node import Node

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return 

    def height(self, key):
        if key == None:
            return 0
        return max(self.height(key.left), self.height(key.right)) + 1 # AVLTree에서는 높이차가 1보다 크면 안되기 때문에 절대값이 1보다 작거나 같아야함

    def insert(self, key):
        if self.root == None: # root에 None일때 insert되는 key값이 root값으로 들어감
            self.root = Node(key)
            v = self.root
            return v.key
        else:
            v = self.root
            while True:
                if key < v.key: # insert되는 key값이 v.key랑 비교
                    if v.left == None:
                        v.left = Node(key)
                        break
                    else:
                        v = v.left
                else:
                    if v.right == None:
                        v.right = Node(key)
                        break
                    else:
                        v = v.right
            return v.key

    def search(self, key):
        v = Node(key)
        if self.root == None: #
            return 
        else:
            v = self.root
            while True:
                if key == v.key:
                    return v.key
                else:
                    if key < v.key: # key값이 v.key값보다 작을때 왼쪽 노드에서 확인
                        if v == v.left:
                            return v.left
                        elif v.left == None:
                            return 'Not Found'
                        else:
                            v = v.left
                    else: # key값이 v.key값보다 클 때 오른쪽 노드에서 확인
                        if key == v.right:
                            return v.right
                        elif v.right == None:
                            return 'Not Found'
                        else:
                            v = v.right

    def delete(self, key):
        v = self.search(key)
        p = v.parent
        if self.root == None:
            return False
        else:
            if v.left == None and v.right == None: # 양쪽 다 자식노드가 없을 때
                return None
            elif v.left != None and v.right == None: # 왼쪽 자식노드만 있을 때
                if key < v.key:
                    p = v
                    v = v.left
            elif v.left == None and v.right != None: # 오른쪽 자식노드만 있을 때
                if key > v.key:
                    p = v
                    v = v.right
            else: #양쪽 다 자식노드가 있을 때
                p = v
                b = v.right
                while b.left:
                    p = b
                    b = b.left
                v.key = b.key
                if p.left == b:
                    p.left = b.right
                else:
                    p.right = b.right
            return True


    