'''
基数排序：算法运行之前要清楚数据的具体范围
大循环的次数是输入元素的最大位数。依次按照个位、十位、百位...进行排序。
内层循环的次数是输入数组的长度。创建cnt二维数组，每个数组内部有若干个“桶“(一位子数组)。
每次大循环后，要把cnt中桶数组的元素按顺序传到nums中，然后清空桶元素，进行二次大循环。
一直到最高位排序结束。
'''
import numpy as np


def radix_sort(nums, size):
    for i in range(3):
        # 每次大循环清空cnt数组
        # cnt一维子数组的个数设置为10的原因是，0~9 这10种数字
        cnt = [[] for _ in range(10)]
        # 将nums中元素位数(个、十、百...)的值按照索引放到cnt中相应的位置
        for j in range(size):
            cnt[get(nums[j], i)].append(nums[j])
        # 所有的数值为0~9共10种情况
        k = 0
        for i in range(10):
            for x in cnt[i]:
                nums[k] = x
                k += 1
    return nums


def get(x, i):
    while i > 0:
        x //= 10
        i -= 1
    return x % 10


if __name__ == '__main__':
    nums = [124, 32, 5, -5, -100]
    nums = nums + np.array([100] * 5)
    size = len(nums)
    res = radix_sort(nums, size)
    res = res + np.array([-100] * 5)
    print(res)
