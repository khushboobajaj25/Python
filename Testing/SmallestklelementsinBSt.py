

class Node:

   def __init__(self,data):
       self.data = data
       self.left = None
       self.right = None




def insert_in_BST(root,val):
    if root == None:
        return Node(val)
    elif root.data == val:
        return root
    elif val<root.data:
       root.left = insert_in_BST(root.left,val)

    elif val > root.data:
        root.right = insert_in_BST(root.right,val)
    return root

def inorder (root,array):
    if root!=None:
        inorder(root.left,array)
        array.append(root.data)
        inorder(root.right,array)

T = int(input())
for i in range(T):
    N = int(input())
    array = []
    input_list = [int(x) for x in input().split() ]
    K = int(input())
    for j in range(len(input_list)):
        if j==0:
            r = Node(input_list[j])
            insert_in_BST(r,input_list[j])
        else:
             insert_in_BST(r,input_list[j])

    inorder(r,array)
    sum = 0
    for j in range(len(array)):
        if(j<K):
            sum+=array[j]
    print(sum)
