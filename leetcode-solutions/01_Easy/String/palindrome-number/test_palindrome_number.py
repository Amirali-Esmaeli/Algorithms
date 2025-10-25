from solution_palindrome_number import Solution


def test_example_case():
    x = 121
    result = Solution().isPalindrome(x)
    assert result == True


def test_no_solution():
    x = -121
    result = Solution().isPalindrome(x)
    assert result == False
