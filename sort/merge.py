# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#     middle = len(arr) // 2
#     left, right = arr[:middle], arr[middle:]
#     return sort(merge_sort(left), merge_sort(right))
#
# def sort(left, right):
#     """归并排序"""a
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     while left:
#         result.append(left.pop(0))
#     while right:
#         result.append(right.pop(0))
#     return result


def merge_sort(arr):
    """归并排序"""
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    """合并left 和 right"""
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))

    while right:
        result.append(right.pop(0))

    return result
