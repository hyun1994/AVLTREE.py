from Node import Node
from BST import BST
from AVLTREE import AVLTREE 
import math

if __name__ == '__main__':
    array = [4,5,3,2,6,7,1,8]
    bst = BST()
    
    for v in array:
         bst.insert(v)
    
    print(bst.root)
    print(bst.search(9))
    print()
    print(bst.delete(8))
    print('preorder: ', end=' ') ; Node.preorder(bst.root)