'''
计数排序：不需要比较的一种排序算法，但是必须知道排序数的具体范围。
此外还要额外创建一个cnt数组存放每个元素出现的次数。
假设，nums数组的范围为0到100，则cnt数组索引为0的元素存放nums
数组中数值为0的元素出现的次数，cnt数组索引为1的元素存放nums中数值为
1的元素的次数......
若待排数组中含有负数，需要预处理，即将数组所有元素减数组最小的元素，
这样保证数组所有元素非负，拍完序之后再加回相应的值即可。
因为cnt数组的索引是从0开始的。
'''

import numpy as np


def counting_sort(nums, size):
    # cnt的维度大小为nums中最大值和最小值的差加一
    # 计数排序cnt矩阵中索引为几，它的值就是几。弊端就是若输入数据的值过大cnt索引将很大，导致维度很大。
    cnt = [0 for _ in range(7)]
    k = 0
    # 构建cnt数组
    for i in range(size):
        cnt[nums[i]] += 1
    for i in range(len(cnt)):
        while cnt[i]:
            nums[k] = i
            k += 1
            cnt[i] -= 1
    return nums


if __name__ == '__main__':
    nums = np.array([1, 4, 2, 1, 3, -1, -1, -2])
    size = len(nums)
    nums = nums + np.array([2] * size)
    res = counting_sort(nums, size) + np.array([-2] * size)
    print(res)
