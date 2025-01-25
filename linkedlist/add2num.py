# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def traves_linkd(l1):
        next = l1.next
        number = 0
        power = 0
        while(next is not None):
            number = number + l1.val*10**power
        print(number)

            
