# Definition for singly-linked list.
import collections

#%% ListNode 클래스 생성
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#%% 정답
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head

        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            # node.val = node.next.val
            # node.next.val = node.val
            node = node.next.next

        return head

def makeNode(lst):
    res = ptr = ListNode()
    for item in lst:
        ptr.next = ListNode(item)
        ptr = ptr.next

    return res.next

if __name__ == "__main__":
    sol = Solution()
    head = makeNode([1,2,3,4,5])
    ans = sol.swapPairs(head)
    while ans:
        print(ans.val, end=' ')
        ans = ans.next
