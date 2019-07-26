#快速排序

#以right为基准，将小于它的数放在其左边，将大于它的数放在其右边,返回基准数的坐标
def partition(nums,left,right):
    j=left
    i=j-1
    r=nums[right]
    while j<=right:
        if nums[j]<=r:
            i+=1
            tmp=nums[i]
            nums[i]=nums[j]
            nums[j]=tmp
        j+=1
    return i

def sort_quick(nums,left,right):
    if left<right:
        index=partition(nums,left,right)
        sort_quick(nums,left,index-1)
        sort_quick(nums,index+1,right)
    return nums

nums=[2,8,7,1,3,5,6,4]
print(sort_quick(nums,0,len(nums)-1))