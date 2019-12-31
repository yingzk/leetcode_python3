from sort.bubble import bubble
from sort.insertion import insertion
from sort.merge import merge_sort
from sort.select import select

if __name__ == '__main__':
    raw_arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('冒泡排序', '-' * 20)
    bubble(raw_arr)
    print('Bubble sort end', '-' * 20, '\n')

    raw_arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('选择排序', '-' * 20)
    insertion(raw_arr)
    print('Insertion sort end', '-' * 20, '\n')

    raw_arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('插入排序', '-' * 20)
    select(raw_arr)
    print('Select sort end', '-' * 20, '\n')

    raw_arr = [3, 2, 4, 7, 1]
    print('归并排序', '-' * 20)
    print('原始', raw_arr)
    result = merge_sort(raw_arr)
    print(result)
    print('Merge sort end', '-' * 20, '\n')
