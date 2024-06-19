import math
# Data Structure

class Stack:

    def __init__(self):
        self.__items = []

    def push(self, ele):
        self.__items.append(ele)

    def pop(self):
        return self.__items.pop() if len(self) > 0 else -1

    def peek(self):
        return self.__items[-1]

    def isempty(self):
        return False if self.__items else True

    def make_empty(self):
        self.__items.clear()

    def __len__(self):
        return len(self.__items)


class Queue:
    def __init__(self):
        self.item = []

    def push(self, data):
        self.item.append(data)

    def pop(self):
        return self.item.pop(0)

    def peek(self):
        return self.item[0]

    def is_empty(self):
        return True if self.item else False

    def __str__(self):
        return f"{self.item}"

    def __len__(self):
        return len(self.item)


class Node:
    def __init__(self,data = None,next = None) -> None:
        self.__data,self.__next = data,next
    def set_data(self,data):
        self.__data = data
        return self
    def set_next(self,next):
        self.__next = next
        return self
    
    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next
    
    def __del__(self):
        del self
    
    def __str__(self) -> str:
        return f'data:{self.__data}'

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def insert_at_first(self,data = None):
        if self.head:
            self.head = Node(data,self.head)
        else:
            self.head = self.tail = Node(data)
        self.len += 1
    
    def insert_at_end(self,data):
        if self.tail:
            self.tail.set_next(Node(data))
            self.tail = self.tail.get_next()
        else:
            self.head = self.tail = Node(data)
        self.len += 1

    def delete_at_last(self):
        if self.head:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.get_next()
            self.tail,temp = temp,self.tail
            del self.tail
            self.len += 1
        else:
            return None
    
    def delete_at_first(self):
        if self.head:
            self.head,temp = self.head.next,self.head

    
    
    
    def __str__(self):
        if self.head:
            temp = self.head
            a = []
            while temp!=None:
                a.append(temp.get_data())
                temp = temp.get_next()
            return f'{a}'
        else:
            return f'{None}'    
    
    def __len__(self):
        return self.len

#play with numbers:

def min(ls,start=0,end=None):
    end = (end if end else len(ls))
    min_value = math.inf
    for i in range(0,len(ls)):
        if ls[i] < min_value:
            min_value = ls[i]
    return min_value

def min_index(ls,start,end = None):
    end = (end if end else len(ls))
    index = start
    for i in range(start,end):
        if ls[i] < ls[index]:
            index = i
    return index

def max_index(ls,start=0,end=None):
    end = (end if end else len(ls))
    index = start
    for i in range(start,len(ls)):
        if ls[i] > ls[index]:
            index = i
    return index

def max(ls,start=0,end=None):
    end = (end if end else len(ls))
    max_value = -1 * math.inf
    for i in range(0,len(ls)):
        if ls[i] > max_value:
            max_value = ls[i]
    return max_value

def merge(list1,list2):
    ls = []
    while list1 and list2:
        if list1 and list2[0] >= list1[0]:
            ls.append(list1.pop(0))
        else:
            ls.append(list2.pop(0))
    if list1:
        ls = ls + list1
    if list2:
        ls = ls + list2
    return ls 

#Sorting

def bubble_sort(ls,start = 0,end =None, reversed = False):
    end = (end if end else len(ls))
    for i in range(start,end-1):
        for j in range(i+1,end):
            if not reversed:
                if ls[i] > ls[j]:
                    ls[i],ls[j] = ls[j],ls[i]
            else:
                if ls[i] < ls[j]:
                    ls[i],ls[j] = ls[j],ls[i]
    
def selection_sort(ls,start = 0,end = None,reversed = False):
    end = (end if end else len(ls))
    for i in range(start,end-1):
        index = (min_index(ls,i) if not reversed else max_index(ls,i))
        ls[i], ls[index] = ls[index], ls[i]

def insertion_sort(ls,start = 0, end =None,reversed = False):
    end = (end if end else len(ls))
    for i in range(start+1,end):
        for j in range(i,0,-1):
          if reversed:
              if ls[j] > ls[j-1]:
                   ls[j] , ls[j-1] = ls[j-1],ls[j]
              else:
                  break
          else:
              if ls[j] < ls[j-1]:
                   ls[j] , ls[j-1] = ls[j-1],ls[j]
              else:
                  break
              
def quick_sort(ls,start,end,reversed = False):
  if start < end:
    j = start - 1 
    i = start
    pivot = end
    while i < end:
        if reversed:
            if ls[i] >= ls[pivot]:
                j += 1
                ls[i],ls[j] = ls[j],ls[i]
        else:
            if ls[i] <= ls[pivot]:
                j += 1
                ls[i],ls[j] = ls[j],ls[i]
        i+=1
    j+=1
    ls[i],ls[j] = ls[j],ls[i]
    quick_sort(ls,start,j-1,reversed)
    quick_sort(ls,j+1,end,reversed)
        
            

# def merge_sort(ls,low,high):
#     if low < high:
#         mid = (low + high)//2
#         ls[low:mid] = merge_sort(ls,low,mid)
#         ls[mid:high] = merge_sort(ls,mid+1,high)
#         return merge(ls[low:mid],ls[mid:high])
     
def merge_sort(ls, low, high):
    if low < high:
        mid = (low + high) // 2
        left_half = merge_sort(ls, low, mid)
        right_half = merge_sort(ls, mid + 1, high)
        return merge(left_half, right_half)
    else:
        return ls[low:high + 1]



    


              


