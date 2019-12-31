from sort.bubble import bubble
from sort.insertion import insertion

if __name__ == '__main__':
    raw_arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('Bubble sort', '-' * 20)
    bubble(raw_arr)
    print('Bubble sort end', '-' * 20, '\n')

    raw_arr = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print('Insertion sort', '-' * 20)
    insertion(raw_arr)
    print('Insertion sort end', '-' * 20, '\n')
