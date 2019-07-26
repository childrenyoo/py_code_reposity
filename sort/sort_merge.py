#归并排序
#时间复杂度O(nlogn) 空间复杂度O(n)
def sort_merge(nums):
    if len(nums)==2:
        return merge(nums[:1],nums[1:])
    if len(nums)==1:
        return nums
    left=0
    right=len(nums)
    mid=(left+right)//2
    nums1=sort_merge(nums[left:mid])
    nums2=sort_merge(nums[mid:right])
    return merge(nums1,nums2)

def merge(nums1,nums2):
    i=0
    j=0
    res=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i+=1
        else:
            res.append(nums2[j])
            j+=1
    if i==len(nums1):
        for k in nums2[j:]:
            res.append(k)
    else:
        for k in nums1[i:]:
            res.append(k)
    return res

nums=[4,5,8,1,2,2,3,7,6,6]
print(sort_merge(nums))