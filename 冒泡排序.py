'''
冒泡排序
内层循环减i 是因为每一次外层循环i时，一定会把最大的排到最后一个位置，
当第二次外层循环的时候，一定会把第二大的排到倒数第二个位置，故内层循环
不需要再考虑倒数i个数
'''


def bubble_sort(nums):
    for i in range(len(nums) - 1):
        flag = True  # 索引交换一次，标志转换一次
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = False
        if flag:  # 标志不转换了，说明数组已经有序，可以提前结束循环
            return nums


nums = [5, 3, 7, 1, 8, 2]
print(bubble_sort(nums))
