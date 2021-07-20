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
        while v: # search 함수 작동원리
            if v.key == key:
                break
            elif v.key > key:
                p = v
                v = v.left
            else:
                p = v
                v = v.right

        if v.left == None and v.right == None:  # 양쪽 다 자식노드가 없을때
            if key < p.key:
                p.left = None
            else:
                p.right = None
            

        elif v.left != None and v.right == None: # 왼쪽 자식노드만 있을때
            if key < p.key:
                p.left = v.left
            elif key > p.key:
                p.right = v.left
            
        elif v.left == None and v.right != None: # 오른쪽 자식노드만 있을 때
            if key < p.key:
                p.left = v.right
            elif key > p.key:
                p.right  = v.right
            
        elif v.left != None and v.right != None: # 양쪽 다 자식노드가 있을 때
            if key < p.key: # 부모노드 키값이 키값보다 클때 왼쪽 노드에서 작업
                a = v.left # a는 재조정노드
                pa = v # a의 부모노드는 v
                while a.left != None: # 재조정할 노드 중 작은 값 찾기
                    pa = a
                    a = a.left
                if a.right != None:
                    pa.left = a.right
                else:
                    if pa == v:
                        pa.right = None
                    else:
                        pa.left = None
                p.left = a
                a.right = v.right
                a.left = v.left
            elif key > p.key: # 부모노드 키값이 키값보다 작을 때 오른쪽 노드에서 작업
                a = v.right
                pa = v
                while a.right != None:
                    pa = a
                    a = a.right
                if a.left != None:
                    pa.right = a.left
                else:
                    if pa == v:
                        pa.left = None
                    else:
                        pa.right = None
                p.right = a
                a.right = v.right
                a.left = v.left
        return True