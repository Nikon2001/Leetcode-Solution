# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        reverse_list = None
        while fast != None and fast.next != None:
            temp = slow
            slow = slow.next
            fast = fast.next.next
            temp.next = reverse_list
            reverse_list = temp
        if fast != None:
            slow = slow.next
        while reverse_list != None and reverse_list.val == slow.val:
            reverse_list = reverse_list.next
            slow = slow.next
        return reverse_list is None