from Node import Node
from BST import BST
class AVLTREE(BST):
    def __init__(self):
        self.root = None
        self.height = 1
        self.balance = 0

    def Height(self, node):
        node = self.root
        if node:
            return self.height
        else:
            return 0

    def Balance(self, node):
        node = self.root
        if node:
            return self.Height(node.left) - self.Height(node.right)
        else:
            return 0 

    def Insert(self,key):
        if self.root == None: # root에 None일때 insert되는 key값이 root값으로 들어감
            self.root = Node(key)
            node = self.root
            return node.key
        else:
            node = self.root
            while True:
                if key < node.key: # insert되는 key값이 node.key랑 비교
                    if node.left == None:
                        node.left = Node(key)
                        
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = Node(key)
                        break
                    else:
                        node = node.right
            self.height =  max(self.Height(node.left), self.Height(node.right)) + 1
            balance = self.Balance(node)

            if balance > 1 and key < node.left: # LL 양수가 나오면 왼쪽 서브트리가 더 높다는 의미
                return self.Rrotate(node)
            if balance < -1 and key > node.right: # RR 음수가 나오면 오른쪽 서브트리가 더 높다는 의미
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
        x = node.left # node노드가 x노드의 부모노드이면서 x노드는 node보다 작은 값
        if x == None:
            return
        y = x.right # x노드의 값보다 큰 값의 노드를 y로 설정
        x.parent = self.parent # 회전을 하면 node의 부모노드는 x의 부모노드로 변경
        if self.parent: # x.parent = self.parent로 변경 되었기 때문에 node가 왼쪽 자식노드인지 오른쪽 자식노드인지 설정
            if self.parent.left == node:
                self.parent.left = x
            else:
                self.parent.right = x
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
        x.parent = self.parent # 회전을 하면 node의 부모노드는 x의 부모노드로 변경
        if self.parent: # x.parent = self.parent로 변경 되었기 때문에 node가 왼쪽 자식노드인지 오른쪽 자식노드인지 설정
            if self.parent.left == node:
                self.parent.left = x
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

            if node.left == None and node.right == None: # 양쪽 자식노드가 없을 때
                if key > self.parent.key:
                    self.parent.right = None
                elif key < self.parent.key:
                    self.parent.left = None

            elif node.left != None and node.right == None: # 왼쪽 자식노드만 있을 때
                if key < self.parent.key:
                    self.parent.left = node.left
                elif key > self.parent.key:
                    self.parent.right = node.right
        
            elif node.left == None and node.right != None: # 오른쪽 자식노드만 있을 떄
                if key < self.parent.key:
                    self.parent.left = node.right
                elif key > self.parent.key:
                    self.parent.right = node.right
       
            elif node.left != None and node.right != None: # 양쪽 자식노드가 있을 때                
                if key < self.parent.key: # 왼쪽 서브트리 확인
                    self.child = node.right # child는 재조정노드
                    self.pchild = node # pchild는 chlid의 부모노드
                    while self.child.left != None: # 재조정한 child의 오른쪽 노드에서 반복해서 가장작은값 찾기
                        self.pchild = self.child
                        self.child = self.child.left # 반복하다가 child.left = None이 될때 반복문 종료
                    if self.pchild.left != None:
                        self.child.left = node.left
                    self.parent.left = self.child

                elif key >= self.parent.key: # 오른쪽 서브트리 확인
                    self.child = node.right # child는 재조정 노드
                    self.pchild = node # pchild는 chlid의 부모노드
                    while self.child.left != None: # 재조정한 child의 오른쪽 노드에서 반복해서 가장작은값 찾기
                        self.pchild = self.child
                        self.child = self.child.left # 반복하다가 child.left = None이 될때 반복문 종료                                        
                    if self.pchild.left != None:
                        self.child.left = node.left
                    elif self.pchild.left == None:
                        self.child.left = None
                    self.parent.right = self.child
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