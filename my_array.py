import array_1
import random

""" 
File: 引用数组扩展方法文件array_1.py 增强数组类型
Created Time: 2024-3-2
具体方法为: 
array_1.random_access(nums) 在 nums 中获取随机元素
array_1.extend(nums, 3)     将数组长度扩展3
array_1.insert(nums, 6, 3)  在索引 3 处插入数字 6 
array_1.remove(nums, 2)     删除索引 2 处的元素
array_1.traverse(nums)      遍历现在nums
array_1.find(nums, 54)      在 nums 中查找元素 54 ，得到索引
"""

if __name__ == "__main__":
    # 初始化数组
    arr = [0] * 5
    print("数组 arr =", arr)
    nums = [1, 30, 22, 54, 41]
    print("数组 nums =", nums)

    # 随机访问
    random_num: int = array_1.random_access(nums)
    print("在 nums 中获取随机元素", random_num)

    # 长度扩展
    nums: list[int] = array_1.extend(nums, 3)
    print("将数组长度扩展至 8 ，得到 nums =", nums)

    # 插入元素
    array_1.insert(nums, 6, 3)
    print("在索引 3 处插入数字 6 ，得到 nums =", nums)

    # 删除元素
    array_1.remove(nums, 2)
    print("删除索引 2 处的元素，得到 nums =", nums)

    # 遍历数组
    array_1.traverse(nums)
    print("遍历现在nums =", nums)

    # 查找元素
    index: int = array_1.find(nums, 54)
    print("在 nums 中查找元素 54 ，得到索引 =", index)


