# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values = sorted(values)

        dummy = ListNode(0)
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

        