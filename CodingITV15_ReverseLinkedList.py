# Definition for singly-linked list.
import collections

#%% ListNode 클래스 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%% 정답
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        prev = None

        while node:
            next = node.next
            node.next = prev

            prev = node
            node = next

        return prev

def makeNode(lst):
    res = ptr = ListNode()
    for item in lst:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return res.next

if __name__ == "__main__":
    sol = Solution()
    head = makeNode([1,2,3,4,5])
    ans = sol.reverseList(head)
    while ans:
        print(ans.val, end=' ')
        ans = ans.next
