from library import Queue
class Node:
  def __init__(self,data,right=None,left=None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return f'{self.data}'

def preorder(root):
  if not root:
    return
  print(root.data)
  preorder(root.left)
  preorder(root.right)

def postorder(root):
  if not root:
    return
  preorder(root.left)
  preorder(root.right)
  print(root.data)

def inorder(root):
  if not root:
    return
  preorder(root.left)
  print(root.data)
  preorder(root.right)

queue = Queue()
def breath_first_Search(root,left_view = False,right_view = False):
  l_view = []
  r_view = []
  bst = []
  if root:
    queue.push(root)
    queue.push(None)
    while queue.peek():
      l_view.append(queue.peek().data)
      while queue.peek():
        temp = queue.pop()
        print(temp.data, end = " ")
        if temp.left:
          queue.push(temp.left)
        if temp.right:
          queue.push(temp.right)
      r_view.append(temp.data)
      print()
      queue.push(None)
      queue.pop()
  if right_view and left_view:
    return f'{l_view},{r_view}'
  elif right_view:
    return f'{r_view}'
  elif left_view:
    return f'{l_view}'
  

def left_view(root):
  ls = []
  if root:
    queue.push(root)
    queue.push(None)
    while queue.peek():
      ls.append(queue.peek().data)
      while queue.peek():
        temp = queue.pop()
        print(temp.data, end = " ")
        if temp.left:
          queue.push(temp.left)
        if temp.right:
          queue.push(temp.right)
      print()
      queue.push(None)
      queue.pop()
  return ls

# def right_view(root):
#   ls = []
#   if root:
#     queue.push(root)
#     queue.push(None)
#     while queue.peek():
#       while queue.peek():
#         temp = queue.pop()
#         print(temp.data, end = " ")
#         if temp.left:
#           queue.push(temp.left)
#         if temp.right:
#           queue.push(temp.right)
#       ls.append(temp.data)
#       print()
#       queue.push(None)
#       queue.pop()
#   return ls


d = {}
def top_view(root,key = 0):
  if not root:
    return
  if key in d:
    d[key] = root.data
    top_view(root.left,key-1)
    top_view(root.right,key+1)
  

def height(root):
  if root:
    LH = height(root.left)
    RH = height(root.right)
    return max(LH,RH) + 1
  return 0

ls = []
def leaf_node(root):
    if not root:
      return 
    if not root.left and not root.right:
      print(root.data,end =" ")
      # ls.append(root.data)
      return
    leaf_node(root.left)
    leaf_node(root.right)

if __name__ == '__main__':
  # root = Node(1)
  # root.left = Node(2)
  # root.right = Node(3)
  # root.left.right = Node(4)
  # root.left.left = Node(5)
  # root.right.left = Node(6)
  # root.right.right = Node(7)
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.left=Node(4)
  root.left.right=Node(5)
  root.right.left=Node(6)
  root.right.right=Node(7)
  root.left.right.left=Node(9)
  root.left.right.right=Node(10)
  root.right.right.right=Node(11)
  root.left.right.left.left=Node(12)
  root.left.right.left.left.left=Node(78)
  root.left.right.left.right=Node(13)
  # breath_first_Search(root)
  # print(left_view(root))
  print("left_view,Right view:",breath_first_Search(root,right_view=True,left_view=True))
  
  # print("Preorder")
  # preorder(root)
  # print("Postorder")
  # postorder(root)
  # print("Inorder")
  # breath_first_Search(root)
  # top_view(root)
  # for i in sorted(d):
  #   print(d[i])
  # print("leaf nodes are :")
  # leaf_node(root)
  # inorder(root)

