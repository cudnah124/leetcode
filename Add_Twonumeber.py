class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create linked list [2, 4, 3]
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create linked list [5, 6, 4]
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 is not None or l2 is not None or carry != 0:
        digit1 = l1.val if l1 is not None else 0
        digit2 = l2.val if l2 is not None else 0

        sum = digit1 + digit2 + carry
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return dummy_head.next  

result = add_two_numbers(l1, l2)

while result is not None:
    print(result.val, end=' ')
    result = result.next