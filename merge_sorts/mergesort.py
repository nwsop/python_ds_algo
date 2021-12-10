my_list = [1,3,2,4,9,7,8,5,6]

def merge_sort(items):
    if len(items) <= 1:
        return items
    mid_idx = len(items) // 2
    left_items = items[:mid_idx]
    right_items = items[mid_idx:]

    left_sorted = merge_sort(left_items)
    right_sorted = merge_sort(right_items)

    return merge(left_sorted, right_sorted)

def merge(left, right):
    results = []
    while (left and right):
        if left[0] < right[0]:
            results.append(left[0])
            left.pop(0)
        else:
            results.append(right[0])
            right.pop(0)
    if left:
        results += left
    if right:
        results += right
    return results

print(merge_sort(my_list))

