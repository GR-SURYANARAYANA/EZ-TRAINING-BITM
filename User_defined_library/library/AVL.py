class Node:
  def __init__(self,value,left = None,right=None,height = 1):
    self.value = value
    self.left = left
    self.right = right
    self.height = height


def inorder(root):
  if root:
    inorder(root.left)
    print(root.value)
    inorder(root.right)


def get_height(root):
  if root:
    return root.height
  return 0

def get_BF(root):
  if root:
    return get_height(root.left) - get_height(root.right)
  return 0


# Rotation Types
def right_rotation(A):
  B = A.left
  temp = B.right
  B.right = A
  A.left = temp
  # B.left,A.left = A,B.left
  A.height = 1 + max(get_height(A.left),get_height(A.right))
  B.height = 1 + max(get_height(B.left),get_height(B.right))
  return B

def left_rotation(A):
  B = A.right

  temp = B.left
  B.left = A
  A.right = temp
  # B.right,A.right = A,B.right
  A.height = 1 + max(get_height(A.left),get_height(A.right))
  B.height = 1 + max(get_height(B.left),get_height(B.right))
  return B
  
def insert(root,super):
  if not root:
    return Node(super)
  
  if super < root.value:
    root.left = insert(root.left,super)
  else:
    root.right = insert(root.right,super)
 
  # calculate height of the tree every time and update the height of tree
  root.height = 1 + max(get_height(root.left),get_height(root.right))
 
  #calculate balanace factor
  BF = get_BF(root)
 
  #if balance required then balance the tree using following conditions
  

  if BF < -1 and super < root.right.value:
    root.right = right_rotation(root.right)
    return left_rotation(root)
  
  #
  if BF < -1 and super > root.right.value:
    return left_rotation(root)
  
  #RR
  if BF > 1 and super < root.left.value:
    return right_rotation(root)
  
  #RL
  if BF > 1 and super > root.left.value:
    root.left = left_rotation(root.left)
    return right_rotation(root)
  return root
  

if __name__=="__main__":
  root = None
  VL = [19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
  for i in VL:
    root = insert(root,i)
  inorder(root)