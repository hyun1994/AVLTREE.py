from Node import Node
from BST import BST
from AVLTREE import AVLTREE 
import math

if __name__ == '__main__':
    array = [5,3,7,2,4,6,8,1,9]
    bst = BST()
    
    for i in array:
         bst.insert(i)
    
    print(bst.root)
    print(bst.search(9))
    print()
    print('preorder: ', end=' ') ; Node.preorder(bst.root)
    print()
    print('inorder: ', end=' ') ; Node.inorder(bst.root)
    print()
    print('postorder: ', end=' ') ; Node.postorder(bst.root)
    print()
    print(bst.delete(8))
    print(bst.delete(2))
    print('preorder: ', end=' ') ; Node.preorder(bst.root)
