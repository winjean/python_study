#!/usr/bin/python3
# -*- coding: UTF-8 -*-


# 冒泡排序
def bubble_sort(alist):
    # 循环列表长度次数
    for j in range(len(alist) - 1):
        # 循环 比较前一个元素与后一个元素的大小
        for i in range(len(alist) - 1 - j):
            # 判断前一个元素比后一个元素大，元素交换位置
            if alist[i] > alist[i + 1]:
                # 元素交换位置
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    # 返回列表元素
    return alist


# 选择排序
def selection_sort(alist):
    # 循环次数为列表长度-1，且是反向循环
    for j in range(len(alist), 1, -1):
        # 最大值的下标
        max_index = 0
        # 每次循环，找出最大值放在列表最右端，找寻下一个值时，不再需要判断最后一个值大小(最大)
        for i in range(1, j):
            # 判断前后相邻元素的比较，从第一个元素开始比较
            if alist[max_index] < alist[i]:
                # 当条件不满足时，max_index索引被赋值下一个元素i,i则+1 继续下一轮循环比较
                max_index = i
        # 每次循环一次j，则找到最大元素下标max_index,通过元素下标与列表最后一个元素交换位置
        alist[max_index], alist[j - 1] = alist[j - 1], alist[max_index]

    return alist


def insertion_sort(alist):
    # 循环列表长度
    for i in range(1, len(alist)):

        # 当前元素比有序列表中的所有元素小，插入第一个位置，i-1<0条件不成立，结束wehile循环
        while i > 0:
            # 判断后一个元素小于前一个元素时，元素交换位置
            if alist[i] < alist[i - 1]:
                # 前后元素位置交换
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                # 继续比较与有序列表中的前一个位置元素大小，直到小于前一个位置元素
                i -= 1
            else:
                # 当前元素大于有序列表中最后一个元素时，当前元素位置不动(当前元素大于有序列表中最大值)
                break

    # 返回列表
    return alist


def shell_sort(alist):
    # 增量 每次增量的索引值是列表元素长度的一半
    gap = len(alist) // 2

    # 增量值条件为1时，排序完成
    while gap >= 1:

        # 循环列表长度
        for i in range(gap, len(alist)):

            # alist[i-1]:第一次插入时的有序列表
            # alist[i]:乱序列表中的第一个列表元素
            while i > 0:
                if alist[i] < alist[i - gap]:
                    alist[i], alist[i - gap] = alist[i - gap], alist[i]
                    i -= gap
                else:
                    break

        # 增量值取一半
        gap //= 2
    return alist


def quick_sort(alist, start, end):
    low = start
    high = end

    # 当索引最小值大于最大值，退出递归
    if low > high:
        return

        # 定义列表第一个索引下标为mid值
    mid = alist[low]

    while low < high:
        # 先从列表的最右边，high开始判断
        while low < high:
            # high指向的值大于中间值则元素位置不改变，high-1
            if alist[high] > mid:
                high -= 1
            else:
                # 条件不满足时，交换中间值mid(当前mid为索引0位置的值)
                alist[low] = alist[high]
                break

        # high指针移动后，在移动low指针
        while low < high:
            if alist[low] < mid:
                low += 1
            else:
                # 找到low指针指向的值大于mid中间值时，把当前low的值放入之前high指针对应位置
                alist[high] = alist[low]
                break

    # 当前循环到low指针与high指针重合时，条件不成立，退出循环(low=high)
    alist[low] = mid  # 同alist[high] = mid

    # 递归
    quick_sort(alist, start, high - 1)
    quick_sort(alist, low + 1, end)  # 将基准右侧的子列表进行递归操作

    # 返回最后排序的列表值
    return alist


def merge_sort(alist):
    n = len(alist)
    # 结束递归的条件
    if n <= 1:
        return alist

    # 中间索引
    mid = n//2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])

    # 指向左右表中第一个元素的指针
    left_pointer, right_pointer = 0, 0
    # 合并数据对应的列表：该表中存储的为排序后的数据
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        # 比较最小集合中的元素，将最小元素添加到result列表中
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
    # 当左右表的某一个表的指针偏移到末尾的时候，比较大小结束，将另一张表中的数据（有序）添加到result中
    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result


def main():
    alist = [2, 3, 4, 5, 9, 6, 7]
    print(alist)
    # bubble_sort(alist)
    # selection_sort(alist)
    # insertion_sort(alist)
    # shell_sort(alist)
    # quick_sort(alist, 0, len(alist) - 1)
    alist = merge_sort(alist)
    print(alist)


if __name__ == '__main__':
    main()
