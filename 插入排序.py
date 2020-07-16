'''
插入排序：
从第二个元素开始循环，并把当前元素记为temp。然后进入内层循环，内层循环是从
第二个元素开始一个一个往前查询。如果发现第二个元素的前一个元素比第二个元素大，
那么将前一个元素的值赋予给第二个元素。如果前一个元素的值没有比这个元素大，
那么直接跳出该层循环，并更新外层循环。最后temp值赋给被重新赋值元素的前一个元素。


希尔排序：
它是插入排序的改进版本，和插入排序不同的是它是优先比较距离最远的元素，又叫缩小增量排序。
先定义一个间隔，间隔是动态缩小的，间隔有了之后枚举所有组，在组的内部进行插入排序。
'''


def insert_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = temp
    return nums


'''

    for i in range(1, len(nums)):
        temp = nums[i]
        for j in range(i - 1, -2, -1):
            if nums[j] > temp:
                nums[j + 1] = nums[j]
            else:
                break
        # 相当于把temp赋给了nums[j]
        nums[j + 1] = temp
'''

nums = [5, 3, 7, 1, 8, 2]
print(insert_sort(nums))
