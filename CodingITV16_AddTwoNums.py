# Definition for singly-linked list.
import collections

#%% ListNode 클래스 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%% 정답
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node_A = l1
        node_B = l2



        return node_A + node_B

def makeNode(lst):
    res = ptr = ListNode()
    for item in lst:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return res.next

if __name__ == "__main__":
    sol = Solution()
    head_A = makeNode([2,4,3])
    head_B = makeNode([5,6,4])
    ans = sol.addTwoNumbers(head_A, head_B)
    while ans:
        print(ans.val, end=' ')
        ans = ans.next
