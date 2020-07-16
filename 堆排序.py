'''
根据升序降序选取不同的堆，一般升序选取大根堆，降序选取小根堆。
1.先将无序的序列构建成一个堆，根据升序降序的需求选取大根还是小根堆。
2.将堆顶元素和末尾元素交换，这样最大的元素就会沉底
3.重新调整结构，使其满足堆的特性。继续交换堆顶和末尾元素，直到整个序列有序。
'''


# 每次在顶更新元素
def push_down(heap, size, u):
    '''

    :param heap: 堆
    :param size: 堆的长度
    :param u: 当前元素
    :return:
    '''
    # t 存的是最大值的索引，即根节点和左右儿子之间的最大值。
    # 这里默认heap 索引号从1开始
    t, left, right = u, u * 2, u * 2 + 1
    if left <= size and heap[t] < heap[left]:
        t = left
    if right <= size and heap[t] < heap[right]:
        t = right
    # 若if成立则说明根要和儿子换位置了
    if t != u:
        heap[u], heap[t] = heap[t], heap[u]
        # 继续往下递归直到形成一个堆
        push_down(heap, size, t)
    return heap


# 每次在尾更新元素,每个元素和父节点比较大小
def push_up(heap, u):
    # 如果父节点存在且父节点的值小于子节点的值，就交换位置
    while (u // 2 and heap[u // 2] < heap[u]):
        heap[u // 2], heap[u] = heap[u], heap[u // 2]
        u //= 2
    return heap


# 若每次在中间更新元素，两个函数都调用一下
# push_down()
# push_up()

# 插入一个元素的操作，插到最后一个元素
def insert(heap, size, x):
    size += 1
    heap[size] = x
    push_up(heap, size, x)


# 删除堆顶元素的操作，然后自顶向下调整
def remove_top(heap, size):
    heap[1] = heap[size]
    size -= 1
    push_down(heap, size, 1)


def heap_sort(nums, size):
    # 构建堆自底向上
    for i in range(1, size + 1):
        nums = push_up(nums, i)
    # 调整堆堆自顶向下，每次将堆顶的数和堆尾的数交换
    for i in range(1, size + 1):
        nums[1], nums[size] = nums[size], nums[1]
        size -= 1
        # 每改动一次堆都要重新调整一次
        nums = push_down(nums, size, 1)
    return nums[1:]


if __name__ == '__main__':
    size = int(input('需要排序的个数:'))
    # 数组索引是从零开始的，而堆的序号是从1开始的，故将数组设置成(size+1)维度.
    nums = [0 for _ in range(size + 1)]
    for i in range(1, size + 1):
        nums[i] = int(input('输出数值:'))
    res = heap_sort(nums, size)
    print(res)
