class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build(arr):
    head = tail = None
    for v in arr:
        node = Node(v)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

def addTwo(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.data if l1 else 0
        v2 = l2.data if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

