'''
快速排序思想：（分治）
通过一趟排序将待排数组分成两部分，基准点pivot可以任意取，其中一部分的关键字均比另一部分的小。
当所有大于基准点的元素都位于右半部分，所有小于基准点的元素都放在左半部分。那么开始对两部分
分别进行多次递归操作，直到这两部分分别有序。最后整个数组便有序。
'''
import random


def quick_sort(l, r, nums):
    if l >= r:
        return None
    else:
        i, j = l, r
        # pivot的值可以任意设置
        index = random.randint(l, r)
        pivot = nums[index]
        while i < j:
            # 小于基准点的元素放在左半部分，大于基准点的元素放在右半部分
            # 若大于基准点的元素在正确的区域则尾指针减一
            while nums[j] > pivot:
                j -= 1
            # 若小于基准点的元素在正确的区域则头指针加一
            while nums[i] < pivot:
                i += 1
            # 若发现元素所在区域不正确，则交换这两个元素
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            # 所有元素都在正确的区域后，开始针对区域内部递归排序。
            else:
                # 基准点左半部分内部元素进行排序
                quick_sort(l, j, nums)
                # 基准点右半部分内部元素进行排序
                quick_sort(j + 1, r, nums)
    return nums


if __name__ == '__main__':
    nums = [1, 3, 2, 4, 7, 5]
    l, r = 0, len(nums) - 1
    print(quick_sort(l, r, nums))
