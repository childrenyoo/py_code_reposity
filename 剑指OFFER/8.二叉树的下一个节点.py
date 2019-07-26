# 题目：给定一棵二叉树和其中一个节点，如何找出中序遍历序列的下一个节点？
# 树中的节点除了有左右指针，还有一个指向父节点的指针

#二叉树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.father=None
#1.有右子树：下一个是右子树的最左节点
#2.没右子树，是父节点的左子节点：下一个是父节点
#3.1和2都不是：沿着指向父节点的指针一直向上遍历，
# 直到找到一个节点是它父节点的左子节点，那么下一个就是它的父节点
def getNext(root,node):
    if node.right!=None:
        cur=node.right
        curfather=cur.father
        while cur!=None:
            curfather=cur
            cur=cur.left
        return curfather.val
    if node==node.father.left:
        return node.father.val
    cur=node
    while cur!=None:
        if cur.father!=None and cur==cur.father.left:
            return cur.father.val
        cur=cur.father
    return None

node1=TreeNode(1)
node2=TreeNode(2)
node3=TreeNode(3)
node4=TreeNode(4)
node5=TreeNode(5)
node6=TreeNode(6)
node7=TreeNode(7)
node8=TreeNode(8)
node9=TreeNode(9)

node1.father=None
node1.left=node2
node1.right=node3

node2.father=node1
node2.left=node4
node2.right=node5

node3.father=node1
node3.left=node6
node3.right=node7

node4.father=node2

node5.father=node2
node5.left=node8
node5.right=node9

node6.father=node3

node7.father=node3

node8.father=node5

node9.father=node5
print(getNext(node1,node9))
print(getNext(node1,node7))
print(getNext(node1,node1))
print(getNext(node1,node6))