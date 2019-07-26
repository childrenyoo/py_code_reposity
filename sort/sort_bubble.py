#冒泡排序
def sort_bubble(nums):
    j=len(nums)-1
    while j>0:
        i = 0
        while i<j:
            if nums[i]>nums[i+1]:
                temp=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=temp
            i+=1
        j-=1
    return nums

nums=[4,5,8,1,2,2,3]
sort_bubble(nums)