from Node import Node
from BST import BST
class AVLTREE(BST):
    def __init__(self):
        self.root = None
        self.height = 1
        self.balance = 0

    def Height(self):
        node = self.root
        if node:
            return self.height
        else:
            return 0

    def Balance(self):
        node = self.root
        if not node:
            return 0
        return self.Height(node.left) - self.Height(node.right)

    def Insert(self,key):
        if self.root == None: # root에 None일때 insert되는 key값이 root값으로 들어감
            self.root = Node(key)
            node = self.root
            return node.key
        else:
            node = self.root
            if key < node.key:
                node.left = super(AVLTREE, self).insert(key)
            else:
                node.right = super(AVLTREE, self).insert(key)
            self.height =  max(self.Height(node.left), self.Height(node.right)) + 1
            balance = self.Balance(node)

            if balance > 1 and key < node.left: # LL
                return self.Rrotate(node)
            if balance < -1 and key > node.right: # RR
                return self.Lrotate(node)
            if balance > 1 and key > node.left: #LR
                node.left = self.Lrotate(node.left)
                return self.Rrotate(node)
            if balance < -1 and key < node.right: #RL
                node.right = self.Rrotate(node.right)
                return self.Lrotate(node)

        return node

    def Rrotate(self, key): # 오른쪽으로 이동하는 노드가 z이므로 z가 기준
        node = self.root           
        self.parent = None
        while node: # search함수 역할
            if node.key == key:
                break
            elif key < node.key:
                self.parent = node
                node = node.left
            else:
                self.parent = node
                node = node.right 
        x = node.left # node노드가 x노드의 부모노드이면서 x노드는 z보다 작은 값
        if x == None:
            return
        y = x.right # x노드의 값보다 큰 값의 노드를 y로 설정
        x.parent = node.parent # 회전을 하면 node의 부모노드는 x의 부모노드로 변경
        if node.parent: # x.parent = z.parent로 변경 되었기 때문에 z가 왼쪽 자식노드인지 오른쪽 자식노드인지 설정
            if node.parent.left == node:
                node.parent.left = x
            else:
                node.parent.right = x
        x.right = node # node>x이기 때문에 node는 x의 오른쪽 자식노드
        node.parent = x 
        node.left = y # x<y<node이기 때문에 y는 node의 왼쪽 자식노드
        if y:
            y.parent = node
        if self.root == node: # node가 루트노드였으면 오른쪽으로 회전하면서 node대신 들어가는 x가 루트노드로 변경
            self.root = x
    
    def Lrotate(self, key): # rotateR의 대칭
        node = self.root           
        self.parent = None
        while node: # search함수 역할
            if node.key == key:
                break
            elif key < node.key:
                self.parent = node
                node = node.left
            else:
                self.parent = node
                node = node.right
        x = node.right # node노드가 x노드의 부모노드이면서 node노드는 node보다 큰 값
        if x == None:
            return
        y = x.left # x노드의 값보다 작은 값의 노드를 y로 설정
        x.parent = node.parent # 회전을 하면 node의 부모노드는 x의 부모노드로 변경
        if node.parent: # x.parent = node.parent로 변경 되었기 때문에 node가 왼쪽 자식노드인지 오른쪽 자식노드인지 설정
            if node.parent.left == node:
                node.parent.left = x
            else:
                node.parent.right = x
        x.left = node # node<x이기 때문에 node는 x의 왼쪽 자식노드
        node.parent = x 
        node.right = y # node<y<x이기 때문에 y는 node의 오른쪽 자식노드
        if y:
            y.parent = node
        if self.root == node: # node가 루트노드였으면 왼쪽으로 회전하면서 node대신 들어가는 x가 루트노드로 변경
            self.root = x

    def Delete(self, key):
        if self.root == None: # root에 None일때 insert되는 key값이 root값으로 들어감
            self.root = Node(key)
            node = self.root
            return node.key
        else:
            node = self.root
            if key < node.key:
                node.left = super(AVLTREE, self).delete(key)
            else:
                node.right = super(AVLTREE, self).delete(key)
            self.height =  max(self.Height(node.left), self.Height(node.right)) + 1
            balance = self.Balance(node)

            if balance > 1 and key < node.left: # LL
                return self.Rrotate(node)
            if balance < -1 and key > node.right: # RR
                return self.Lrotate(node)
            if balance > 1 and key > node.left: #LR
                node.left = self.Lrotate(node.left)
                return self.Rrotate(node)
            if balance < -1 and key < node.right: #RL
                node.right = self.Rrotate(node.right)
                return self.Lrotate(node)

        return node