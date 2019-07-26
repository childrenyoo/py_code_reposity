#题目1：给定一个链表的头，将链表反转，返回反转后的头节点
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList1(head):
    cur=head
    prevNode = None
    while cur!=None:
        nextNode=cur.next
        cur.next=prevNode

        prevNode=cur
        cur=nextNode
    return prevNode

#题目2：反转位置m到n之间的链表，如：
#输入: 1->2->3->4->5->NULL, m = 2, n = 4
#输出: 1->4->3->2->5->NULL
def reverseList2(head,m,n):
    index=1
    cur=head
    prev=None
    while index<m:
        prev=cur
        cur=cur.next
        index+=1
    (first,last,next)=reverseCore(cur,n-m+1)

    last.next=next
    if prev!=None:
        prev.next=first
        return head
    else:
        return first

#从头反转1-index的链表
def reverseCore(head,index):
    last=head
    cur = head
    prevNode = None
    i=1
    while i <= index:
        nextNode = cur.next
        cur.next = prevNode

        prevNode = cur
        cur = nextNode
        i+=1
    return prevNode,last,cur#分别是反转后的首、尾、和反转后的下一个节点


node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)
node4=ListNode(4)
node5=ListNode(5)
node6=ListNode(6)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

#测试用例包括空链表、链表只有一个节点、多个节点
head=reverseList2(node1,2,6)
while head!=None:
    print(head.val)
    head=head.next



