'''
归并排序采用分治的思想。若数组有n个元素，用递归把数组分解成2份，再用递归把2个小份，
继续分解，这样就被分成4份，一直到被分解成n份。n份之后开始回溯，从最小份开始从小到大
排序，直到结束。
'''


def merge_sort(num, l, r):
    if l >= r:
        return None
    else:
        mid = (l + r) // 2
        # mid为分割点
        merge_sort(num, l, mid)
        merge_sort(num, mid + 1, r)
        i, j = l, mid + 1
        m = []  # 临时数组，临时存放中间数据
        while i <= mid and j <= r:
            if num[i] <= num[j]:
                m.append(num[i])
                i += 1
            else:
                m.append(num[j])
                j += 1
        while i <= mid:
            m.append(num[i])
            i += 1
        while j <= r:
            m.append(num[j])
            j += 1
    for j in range(len(m)):
        num[l] = m[j]
        l += 1
    return num


if __name__ == '__main__':
    num = [3, 2, 4, 1, 5]
    print(merge_sort(num, 0, len(num) - 1))
