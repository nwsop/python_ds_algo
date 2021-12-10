my_list = [3,1,2,5,4,7,6,8,9]

def bubble_sort(arr):
    for nums in arr:
        for idx in range(len(arr) - 1):
            # To Descend list, switch operand to <
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr

print(bubble_sort(my_list))