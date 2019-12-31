def bubble(arr):
    """bubble sort"""

    arr_len = len(arr)

    for index in range(arr_len):
        # 遍历一遍
        for i in range(1, arr_len - index):
            if arr[i] > arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    print(arr)
