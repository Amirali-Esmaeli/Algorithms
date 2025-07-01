from solution_two_sum import Solution

def test_example_case():
    nums = [2, 7, 11, 15]
    target = 9
    result = Solution().twoSum(nums, target)
    assert sorted(result) == [0, 1]

def test_no_solution():
    nums = [1, 2, 3]
    target = 10
    result = Solution().twoSum(nums, target)
    assert result is None or result == []

def test_duplicate_numbers():
    nums = [3, 3]
    target = 6
    result = Solution().twoSum(nums, target)
    assert sorted(result) == [0, 1]
