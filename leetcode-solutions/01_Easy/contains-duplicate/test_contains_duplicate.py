from solution_contains_duplicate import Solution


# result True
def test_contains_duplicate_set():
    nums = [1, 2, 3, 1]
    result = Solution().contains_duplicate_set(nums)
    assert result == True


def test_contains_duplicate_hash_set_result_true():
    nums = [1, 2, 3, 1]
    result = Solution().contains_duplicate_hash_set(nums)
    assert result == True


def test_contains_duplicate_sort_result_true():
    nums = [1, 2, 3, 1]
    result = Solution().contains_duplicate_sort(nums)
    assert result == True


# result False
def test_contains_duplicate_set_result_false():
    nums = [1, 2, 3, 4]
    result = Solution().contains_duplicate_set(nums)
    assert result == False


def test_contains_duplicate_hash_set_result_false():
    nums = [1, 2, 3, 4]
    result = Solution().contains_duplicate_hash_set(nums)
    assert result == False


def test_contains_duplicate_sort_result_false():
    nums = [1, 2, 3, 4]
    result = Solution().contains_duplicate_sort(nums)
    assert result == False
