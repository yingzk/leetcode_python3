def select(arr):
    """select sort"""
    arr_len = len(arr)

    for index in range(arr_len):
        min_num = arr[index]

        for i in range(index + 1, arr_len):
            if arr[i] > min_num:
                arr[i], min_num = min_num, arr[i]
        arr[index] = min_num

    print(arr)
