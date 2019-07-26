#二分查找
#给定有序数组nums，查找target在其中的下标
#如果不存在，返回-1
def binary_search(nums, target):
        left=0
        right=len(nums)-1
        while(right>=left):
            index=(left+right)//2
            if nums[index]==target:
                return index
            elif nums[index]<target:
                left=index+1
            else:
                right=index-1
        return -1
