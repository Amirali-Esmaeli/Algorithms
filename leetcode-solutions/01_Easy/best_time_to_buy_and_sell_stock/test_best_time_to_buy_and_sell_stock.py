from solution_best_time_to_buy_and_sell_stock import Solution


def test_example_case():
    prices = [7,1,5,3,6,4]
    result = Solution().maxProfit(prices)
    assert result == 5

def test_no_profit():
    prices = [7,6,4,3,1]
    result = Solution().maxProfit(prices)
    assert result == 0
