#插入排序
#平均O(n^2)  最好O(n)   最坏O(n^2)   inplace
def sort_insert(nums):
    index=1
    while index<len(nums):
        i=0
        while i<index:
            if nums[i]>nums[index]:
                nums.insert(i,nums[index])
                del nums[index+1]
                break
            i+=1
        index+=1
    return nums

nums=[4,5,8,1,2,2,3,7]
print(sort_insert(nums))