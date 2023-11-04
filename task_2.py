def task_2(nums):
    def count_digits(num):
        count = 0
        while num > 0:
            count += 1
            num //= 10
        return count

    res = 0
    for num in nums:
        if count_digits(num) % 2 == 0:
            res += 1

    return res

nums1 = [12, 345, 2, 6, 7896]
print(task_2(nums1))

nums2 = [555, 901, 482, 1771]
print(task_2(nums2))
