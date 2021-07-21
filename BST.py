from Node import Node

class BST:
    def __init__(self):
        self.root = self.left = self.right = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return 

    def insert(self, key):
        if self.root == None: # root에 None일때 insert되는 key값이 root값으로 들어감
            self.root = Node(key)
            node = self.root
            return node.key
        else:
            node = self.root
            while True:
                if key < node.key: # insert되는 key값이 v.key랑 비교
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
            return node.key

    def search(self, key):
        node = self.root
        while node:
            if node.key == key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False
    
    def delete(self, key):
        node = Node(key)
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
            node.left, node.right = None, None

        elif node.left != None and node.right == None: # 왼쪽 자식노드만 있을 때
            if key < self.parent.key:
                self.parent.left = node.left

        elif node.left == None and node.right != None: # 오른쪽 자식노드만 있을 떄
            if key > self.parent.key:
                self.parent.right = node.right


        elif node.left != None and node.right != None: # 양쪽 자식노드가 있을 때
            if key > self.parent.key: # 오른쪽 서브트리 확인
                self.child = node.right # child는 재조정 노드
                self.pchild = node # pchild는 chlid의 부모노드
                while self.child != None: # 재조정할 노드 찾기
                    self.pchild = self.child
                    self.child = self.child.right
                if self.child:
                    self.parent.right = self.child
                    self.child.right = node.right
                    self.child.left = node.left
            elif key < self.parent.key: # 왼쪽 서브트리 확인
                self.child = self.root.right
                self.pchlid = self.root
                while self.child.right != None:
                    self.pchlid = self.child
                    self.child = self.child.right
                if self.chlid:    
                    self.parent.left = self.child
                    self.child.right = node.right
                    self.child.left = node.left
        return True

