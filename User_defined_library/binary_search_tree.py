from tree import Node,inorder

def insert(ele,root):
  if not root:
    return Node(ele)
  if root.data > ele:
    root.left = insert(ele,root.right)
  elif root.data < ele:
    root.right = insert(ele,root.left)
  return Node(ele)

def create_tree(ls):
  root = None
  for i in ls:
    root = insert(i,root)
  return root

ls = [4,6,7,3,8,2,5,9,1]

root = create_tree(ls)

inorder(root)



