def buying_houses(budget: int, prices: list):
    sort_prices = sorted(prices)
    d = 0
    while budget >= 0 and d < len(prices):
        budget -= sort_prices[d]
        d += 1 if budget >= 0 else 0
    return d


if __name__ == "__main__":
    count, budget = map(int, input().split())
    prices = list(map(int, input().split()))
    print(buying_houses(budget, prices))
