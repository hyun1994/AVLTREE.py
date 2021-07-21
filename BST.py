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
        v = self.root
        while v:
            if v.key == key:
                return True
            elif key < v.key:
                v = v.left
            else:
                v = v.right
        return False
    
    def delete(self, key):
        v = self.root
        p = self.root
        while v: # search함수 역할
            if v.key == key:
                break
            elif key < v.key:
                p = v
                v = v.left
            else:
                p = v
                v = v.right

        if v.left == None and v.right == None: # 양쪽 자식노드가 없을 때
            if key < p.key:
                p.left = None
            else:
                p.right = None
            
        elif v.left != None and v.right == None: # 왼쪽 자식노드만 있을 때
            if key < p.key:
                p.left = v.left
            else:
                p.right = v.left

        elif v.left == None and v.right != None: # 오른쪽 자식노드만 있을 떄
            if key < p.key:
                p.left = v.right
            else:
                p.right = v.right

        elif v.left != None and v.right != None: # 양쪽 자식노드가 있을 때
            if key < p.key: # 왼쪽자식노드 확인
                a = v.right # a는 재조정 노드
                pa = v # pa는 a의 부모노드
                while a.left != None: # 재조정할 노드 찾기
                    pa = a
                    a = a.left
                if a.right != None: # a의 오른쪽 자식이 있을 때
                    pa.left = a.right
                else: # a의 오른쪽 자식이 없을 때
                    if pa == v:
                        pa.right = None
                    else:
                        pa.left = None
                p.left = a
                a.right = v.right
                a.left = v.left

            else: # 오른쪽 자식노드 확인
                a = v.right
                pa = v
                while a.left != None:
                    pa = a
                    a = a.left
                if a.right != None:
                    pa.left = a.right
                else:
                    if pa == v:
                        pa.right = None
                    else:
                        pa.left = None
                p.right = a
                a.right = v.right
                a.left = v.left

        return True

