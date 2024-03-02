import array
import random
if __name__ == "__main__":
    # 初始化数组
    arr = [0] * 5
    print("数组 arr =", arr)
    nums = [1, 30, 22, 54, 41]
    print("数组 nums =", nums)

    # 随机访问
    random_num: int = array.random_access(nums)
    print("在 nums 中获取随机元素", random_num)

    # 长度扩展
    nums: list[int] = array.extend(nums, 3)
    print("将数组长度扩展至 8 ，得到 nums =", nums)

    # 插入元素
    array.insert(nums, 6, 3)
    print("在索引 3 处插入数字 6 ，得到 nums =", nums)

    # 删除元素
    array.remove(nums, 2)
    print("删除索引 2 处的元素，得到 nums =", nums)

    # 遍历数组
    array.traverse(nums)
    print("遍历现在nums =", nums)

    # 查找元素
    index: int = array.find(nums, 54)
    print("在 nums 中查找元素 54 ，得到索引 =", index)


