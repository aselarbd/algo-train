def two_sum(nums: list, target: int) -> list:
    num_map = {}

    for i in range(len(nums)):
        remaining = target - nums[i]

        if remaining in num_map:
            return [num_map[remaining], i]

        num_map[nums[i]] = i


if __name__ == "__main__":
    print(two_sum(nums=[2, 5, 7, 6, 3], target=10))
    # [2, 4]

    print(two_sum(nums=[2, 7, 11, 15], target=9))
    # [0, 1]
