"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given an array of size n, and all values in the array are in the range 1 to n, find all the duplicates.
"""


def find_duplicates(nums):
    numbers = {}
    duplicates = []
    for num in nums:
        if num in numbers and num not in duplicates:
            duplicates.append(num)
        else:
            numbers[num] = True
    return duplicates


if __name__ == "__main__":
    print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))
    # [2, 3]
