''' BS using recursion '''


def binary_search(data: list[int], target: int, low: int,high: int) -> int:


    if low > high:
        return -1
    else:
        mid = low + (high - low)//2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            high = mid -1
            binary_search(data=data, target=target, low=low,high=high)
        else:
            low= mid + 1
            binary_search(data=data, target=target, low=low,high=high)
    return -1
