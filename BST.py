from Node import Node

class BST:
    def __init__(self, key):
        self.key = key
        self.root = self.left = self.right = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return 

    def insert(self, key):
        self.node = self.root # node 설정
        self.parent = None # parent 설정
        while True:
            if self.node.key > key: # node.key값이 key값보다 클 때 왼쪽노드로 insert
                if self.node.left != None:
                    self.parent = self.node
                    self.node = self.node.left
                else:
                    self.node.parent = self.node
                    self.node.left = Node(key)
                    break
            else: # node.key값이 key값보다 크거나 같을때 오른쪽 노드로 insert
                if self.node.right != None:
                    self.parent = self.node
                    self.node = self.node.right
                else:
                    self.parent = self.node
                    self.node.right = Node(key)
                    break

    def search(self, key):
        self.node = self.root # node설정
        while self.node != None: # node가 None이 되기전까지 반복
            if self.node.key == key: # node key값과 key값이 같을 때 true를 리턴하면서 반복문 종료
                return True
            elif self.node.key > key: # node key값이 key값보다 클 때 왼쪽노드에서 searh
                self.node = self.node.left
            else: # node key값이 key값보다 작을 때 오른쪽 노드에서 search
                self.node = self.node.right
        return False # node key값과 key값이 같지 않을 때 트리에 없는 관계로 False로 리턴

    def delete(self, key):
        self.node = self.root # node 설정
        self.parent = None # parent는 node값의 부모이기 때문에 root 부모는 None
        while self.node != None:
            if self.node.key == key: # node key 값과 key값이 같을 때 반복문 종료
                break
            elif self.node.key > key: # node key 값이 key값보다 클 때 왼쪽노드에서 확인
                self.parent = self.node
                self.node = self.node.left
            else: # node key 값이 key값보다 작을 때 오른쪽 노드에서 확인
                self.parnet = self.node
                self.node = self.node.right

        if self.node.left == None and self.node.right == None: # 양쪽 자식노드가 없을 때
            self.node.left, self.node.right = None, None
        
        elif self.node.left != None and self.node.right == None: # 왼쪽 자식노드만 있을 때
            if self.parent.key > key: # 부모노드 값이 key값보다 클 때 왼쪽노드에서 확인
                self.parent.left = self.node.left # node는 삭제하는 node이기 때문에 parent의 왼쪽노드가 node의 왼쪽 노드로 바로 링크

        elif self.node.left == None and self.node.right != None: # 오른쪽 자식노드만 있을 때
            if self.parent.key < key: # 오른쪽노드에서 확인
                self.parent.right = self.node.right # node는 삭제하는 node이기 때문에 parent의 오른쪽노드가 node의 오른쪽 노드로 바로 링크

        elif self.node.left != None and self.node.right != None:
            if self.parent.key < key: # 오른쪽 노드 삭제 일때
                self.child = self.node.right # 자식노드는 node의 오른쪽노드
                self.pchild = self.node # 자식노드의 부모노드는 node
                while self.child.right != None: # 자식노드가 None이 아닐때 반복을 통해 자식노드가 가장 작은값으로 변경
                    self.pchild = self.child  # 자식노드의 부모노드는 node에서 child로 변경
                    self.child = self.child.right # child는 child의 오른쪽노드 링크
                    break
            elif self.parent.key > key:
                self.child = self.node.left
                self.pchild = self.node
                while self.child.left != None:
                    self.pchild = self.node.right
                    self.child = self.node.left
                    break


