#binary search recursive implementation
def binary_search_recursive(target, start, end, data):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        start = mid+1
    else:
        end = mid - 1
    
    return binary_search_recursive(target, start, end, data)

#test code
if __name__ == "__main__":
    li = [i*3 for i in range(11)]
    target =  6
    idx = binary_search_recursive(target, 0, 10, li)

    print(li)
    print(idx)