from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        if head is None:
            return head
        current = head
        while current.next:
            if current.next.val == val:
                if current.next.next:
                    current.next = current.next.next
                else:
                    current.next = None
            else:
                current = current.next
        return head

if __name__ == '__main__':
    sol = Solution()
