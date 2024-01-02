class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        rem = 0
        while l1 or l2:
            d1 = 0
            d2 = 0
            if l1:
                d1 = l1.val
            if l2:
                d2 = l2.val
            sum = d1 + d2 + rem
            rem = sum % 10
            if sum >= 10:
                aux = sum
                sum = rem
                rem = (aux - rem) // 10
            else:
                rem = 0
            ans.val = sum
            if (l1 and l1.next) or (l2 and l2.next):
                ans.next = ListNode()
            elif rem > 0:
                ans.next = ListNode()
            else:
                ans.next = None
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            ans = ans.next
        if rem > 0:
            ans.val = rem
            ans.next = None
        else:
            ans = None
        return head
        