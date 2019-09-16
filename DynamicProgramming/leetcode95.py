# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = []
        for i in range(1, n + 1):
            nums.append(i)
        return self.generateTreeCore(nums)

    def generateTreeCore(self, nums):
        if len(nums) == 2:
            root1 = TreeNode(nums[0])
            root1.right = TreeNode(nums[1])
            root2 = TreeNode(nums[1])
            root2.left = TreeNode(nums[0])
            return [root1, root2]
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        if len(nums) == 0:
            return None
        res = []
        for i in range(len(nums)):
            tmpres = []
            left = self.generateTreeCore(nums[:i])
            right = self.generateTreeCore(nums[i + 1:])
            if not left:
                tmpres.append(TreeNode(nums[i]))
            else:
                for node in left:
                    root = TreeNode(nums[i])
                    root.left=node
                    tmpres.append(root)
            if not right:
                for r in tmpres:
                    res.append(r)
            else:
                for r in tmpres:
                    for node in right:
                        tmp = copy.deepcopy(r)
                        tmp.right = node
                        res.append(tmp)
        return res


s = Solution()
res = s.generateTrees(3)
print(res)
