"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number.
Your solution should ideally be O(n) time and use constant extra space.

Example:
Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
Output: 7
"""


class Solution(object):
    @staticmethod
    def find_single(numbers_list):

        num_list = []

        for number in numbers_list:
            if number in num_list:
                num_list.remove(number)
            else:
                num_list.append(number)

        return num_list[0]


if __name__ == "__main__":
    nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
    print(Solution().find_single(numbers_list=nums))
    # 3
