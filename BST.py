from Node import Node
import math

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
            return v
        else:
            v = self.root
            return v
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

    def delete(self, x): # merging방법= 자식노드를 왼쪽과 오른쪽으로 병합해서 삭제할 노드위치로 옮긴 후 진행
        px = x.parent
        a = x.left # 삭제할 X노드의 왼쪽 자식노드
        b = x.right # 삭제할 x노드의 오른쪽 자식노드
        if a != None:
            c = a # x노드를 삭제하고 대체할 노드
            max = a # 왼쪽 병합된 노드중에서 a가 가장 큼
            while max.right: # None이 나올때까지 반복 
                max = max.right
                if b != None:
                    b.parent = max
                max = b
        else: # a == None 왼쪽노드가 없기 때문에 오른쪽 노드로 진행
            if px != None: # px가 None이 아니기 때문에 c는 루트노드가 아님
                if c:
                    c.parent = px
                if px.key < c.key:
                    px.right = c
                else:
                    px.left = c
            else:
                self.root = c
                if c:
                    c.parent = None

        self.size -= 1 # 노드를 삭제했으므로 사이즈 감소
        return c

