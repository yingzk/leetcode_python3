def insertion(arr):
    """insertion sort"""
    # 这里记住，维护好当前元素左边的子数组
    for index in range(len(arr)):
        for i in range(index - 1, -1, -1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    print(arr)
