def has_pair_with_sum(nums: list[int], target: int):
    is_equal = False
    for n in range(len(nums)):
        for x in range(n + 1, len(nums)):
            result = nums[n] + nums[x]
            if result == target:
                is_equal = True

    return is_equal


print(has_pair_with_sum([1, 3, 5, 7, 9], ))
