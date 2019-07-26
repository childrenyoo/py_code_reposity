#题目：在O(1)时间内删除链表节点
#给定单项链表的头指针和一个节点指针

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#不需要获得被删除节点的上一个节点，只要得到它下一个节点，并将其赋值给被删除节点即可
#需要调用者确保delete确实在以head为头的链表中
def deleteNode(head,delete):
    nextNode=delete.next
    if nextNode==None:
        delete=None
    else:
        delete.val=nextNode.val
        delete.next=nextNode.next
    return head