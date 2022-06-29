class Node:
  def __init__(self, value, right_node = None, left_node = None):
    self.value = value
    self.left = right_node
    self.right = left_node

'''
doubly linked list 이용한 deque 구현
'''

class MyCircularDeque():
  def __init__(self, k: int):
    self.head, self.tail = Node(None), Node(None)
    self.max_size = k
    self.cur_size = 0
    self.head.right = self.tail
    self.tail.left = self.head
    