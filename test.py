from Node import Node
from BST import BST
from AVLTREE import AVLTREE 
import math

if __name__ == '__main__':
    #array = [4,5,3,2,6,7,1,8]
    bst = BST()
    # n1 = Node(10)
    # n2 = Node(20)
    # n3 = Node(30)
    # n4 = Node(40)
    # n5 = Node(50)
    # n6 = Node(60)
    # n7 = Node(70)
    # n8 = Node(80)
    
    # bst.root = n1
    # n1.left = n2
    # n1.right = n3
    # n2.left = n4
    # n2.right = n5
    # n3.left = n6
    # n3.right = n7
    # n4.left = n8
    
    #print('height: ', bst.height(n1))
    #print('preorder: ', end=' ') ; Node.preorder(n1)
    #print('\n inorder: ', end=' ') ; Node.inorder(n1)
    #print('\n postorder: ', end=' ') ; Node.postorder(n1)
    # print(bst.search(90))
    # for v in array:
    #     bst.insert(v)
    bst.insert(4)
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(6)
    bst.insert(7)
    bst.insert(1)
    bst.insert(8)
    print(bst.root)
    print('preorder: ', end=' ') ; Node.preorder(bst.root)
    #print(bst.find_loc(9))
    