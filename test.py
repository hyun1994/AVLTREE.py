from Node import Node
from BST import BST
from AVLTREE import AVLTREE 
import math

if __name__ == '__main__':
    array = [7,5,2,6,4,3,1,8,9]
    avl = AVLTREE()

    
    for i in array:
         avl.Insert(i)
    
    print(avl.root)
    print('preorder: ', end=' ') ; Node.preorder(avl.root)
    print(avl.Lrotate(2))
    print('preorder: ', end=' ') ; Node.preorder(avl.root)