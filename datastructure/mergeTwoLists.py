#将两个有序链表合并为一个有序链表
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p = l1
    q = l2
    new = ListNode(0)
    this = new
    if l1 == None and l2 == None:
        return None
    while p != None and q != None:
        if p.val < q.val:
            this.next = p
            p = p.next
        else:
            this.next = q
            q = q.next
        this = this.next
    if p == None and q != None:
        this.next = q
    elif q == None and p != None:
        this.next = p
    return new.next
