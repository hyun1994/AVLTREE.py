from Node import Node
from BST import BST
class AVLTREE(BST):
    def rotateR(self, z): # 오른쪽으로 이동하는 노드가 z이므로 z가 기준
        if not z: # z가 아니면 그냥 리턴
            return 
        x = z.left # z노드가 x노드의 부모노드이면서 x노드는 z보다 작은 값
        if x == None:
            return
        y = x.right # x노드의 값보다 큰 값의 노드를 y로 설정
        x.parent = z.parent # 회전을 하면 z의 부모노드는 x의 부모노드로 변경
        if z.parent: # x.parent = z.parent로 변경 되었기 때문에 z가 왼쪽 자식노드인지 오른쪽 자식노드인지 설정
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.right = z # z>x이기 때문에 z는 x의 오른쪽 자식노드
        z.parent = x 
        z.left = y # x<y<z이기 때문에 y는 z의 왼쪽 자식노드
        if y:
            y.parent = z
        if self.root == z: # z가 루트노드였으면 오른쪽으로 회전하면서 z대신 들어가는 x가 루트노드로 변경
            self.root = x
    
    def rotateL(self, z): # rotateR의 대칭
        if not z: # z가 아니면 그냥 리턴
            return 
        x = z.right # z노드가 x노드의 부모노드이면서 x노드는 z보다 큰 값
        if x == None:
            return
        y = x.left # x노드의 값보다 작은 값의 노드를 y로 설정
        x.parent = z.parent # 회전을 하면 z의 부모노드는 x의 부모노드로 변경
        if z.parent: # x.parent = z.parent로 변경 되었기 때문에 z가 왼쪽 자식노드인지 오른쪽 자식노드인지 설정
            if z.parent.left == z:
                z.parent.left = x
            else:
                z.parent.right = x
        x.left = z # z<x이기 때문에 z는 x의 왼쪽 자식노드
        z.parent = x 
        z.right = y # z<y<x이기 때문에 y는 z의 오른쪽 자식노드
        if y:
            y.parent = z
        if self.root == z: # z가 루트노드였으면 왼쪽으로 회전하면서 z대신 들어가는 x가 루트노드로 변경
            self.root = x

