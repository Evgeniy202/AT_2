def task_7(arr):
    num_set = set()
    for num in arr:
        if num * 2 in num_set or (num % 2 == 0 and num // 2 in num_set):
            return True
        num_set.add(num)
    return False

arr1 = [10, 2, 5, 3]
print(task_7(arr1))  

arr2 = [3, 1, 7, 11]
print(task_7(arr2)) 
