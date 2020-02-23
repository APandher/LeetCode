
#First Attempt: O(2n) (Two passes through the array)
def maxProfit(self, prices: List[int]) -> int:
    day_profits = []
    profit = 0

    for i in range(0, len(prices) - 1):
        day_profits.append(prices[i+1] - prices[i])

    for i in day_profits:
        if i > 0:
            profit += i

    return profit


#TODO find a better optimized solution
