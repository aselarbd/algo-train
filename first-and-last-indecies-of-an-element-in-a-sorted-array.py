def binary_search_iterative(nums: list, low: int, high: int, key: int, find_first: bool) -> int:
    low = 0
    high = len(nums) - 1
    result = -1

    while high >= low:

        mid = (high + low) // 2

        if key == nums[mid]:
            result = mid
            if find_first:
                high = mid - 1
            else:
                low = mid + 1

        elif key < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return result


def binary_search_recursive(nums: list, low: int, high: int, key: int, find_first: bool) -> int:

    if low > high:
        return -1

    mid = (high + low) // 2

    if key == nums[mid]:
        if find_first:
            if key != nums[mid - 1]:
                return mid
            else:
                high = mid - 1
        else:
            if key != nums[mid + 1]:
                return mid
            else:
                low = mid + 1

    elif key < nums[mid]:
        high = mid-1
    else:
        low = mid+1

    return binary_search_recursive(nums=nums, low=low, high=high, key=key, find_first=find_first)


def get_range(nums: list, value: int) -> list:
    high = len(nums) - 1
    first = binary_search_recursive(nums=nums, low=0, high=high, key=value, find_first=True)
    last = binary_search_recursive(nums=nums, low=0, high=high, key=value, find_first=False)
    return [first, last]


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1, 3, 3, 5, 7, 9, 9, 9, 15]
    target = 1

    solution = get_range(nums=arr, value=target)
    print(solution)
