'''
选择排序:
第一轮找出最小元素，第二轮找出次小元素，第i-1轮找出最大元素
每一次循环一定会找出一个正确位置的元素。循环中若发现，后面的
比前面的小那么交换前后元素。一直到第i-1轮结束。
'''


def chose_sort(nums):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


nums = [5, 3, 7, 1, 8, 2]
print(chose_sort(nums))
