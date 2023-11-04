def task_1(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0 

    max_count = max(max_count, current_count)

    return max_count

nums1 = [1, 1, 0, 1, 1, 1]
print(task_1(nums1))

nums2 = [1, 0, 1, 1, 0, 1]
print(task_1(nums2))
