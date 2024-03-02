
#pythondef
quicksort(arr):
    # 基线条件: 如果数组为空或只有一个元素，那么它已经是排序好的
    if len(arr) < 2:
        return arr
    else:
        # 选择一个基准元素
        pivot = arr[0]
        # 创建两个子数组，一个包含比基准元素小的元素，另一个包含比基准元素大的元素
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        # 返回排序好的子数组，以及可能包含未排序元素的数组
        return quicksort(less) + [pivot] + quicksort(greater)

# 示例
arr = [10, 7, 8, 9, 1, 5]
print("原始数组:", arr)
sorted_arr = quicksort(arr)
print("排序后的数组:", sorted_arr)
