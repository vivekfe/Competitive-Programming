# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return None
        #find length of the linked List
        lastElement= head
        length=1
        while lastElement.next:
            lastElement= lastElement.next
            length+=1
        
        lastElement.next= head
        k=k%length
        splitNode= head
        
        for _ in range(length-k-1):
            splitNode= splitNode.next


        answer = splitNode.next
        splitNode.next = None
        return answer
