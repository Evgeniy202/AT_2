def task_10(nums):
    return sorted(nums, key=lambda x: x % 2)

nums1 = [3, 1, 2, 4]
print(task_10(nums1))  

nums2 = [0]
print(task_10(nums2)) 
