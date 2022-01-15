# Definition for singly-linked list.
import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q = []
        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

class Solution2:
    def isPalidrome(self, head: ListNode) -> bool:
        q = collections.deque()

        if not head:
            return True
        node = head

        while node is not None:
            q.append(node.val)
            node = node.value

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True


if __name__ == "__main__":
    abc = [1,2,3,4,5,1]

    abc.pop()
    abc.pop(0)