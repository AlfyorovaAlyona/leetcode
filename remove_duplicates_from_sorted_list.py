from typing import List
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        if head is None:
            return head
        while current_node.next:
            if current_node.next.val == current_node.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return head

    def print_linked_list(self, head: Optional[ListNode]):
        while head.next:
            print(head.val)
            head = head.next

if __name__ == '__main__':
    list = [1, 1, 2]
    sol = Solution()
