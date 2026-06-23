#ATchaya Vharsne S
investments = [20000, 30000, 40000, 50000]
profits = [25000, 40000, 50000, 55000]
products = ['A', 'B', 'C', 'D']

budget = 100000
n = len(products)

dp = [[0]*(budget + 1) for _ in range(n + 1)]

for i in range(1, n + 1):

    for w in range(budget + 1):

        if investments[i-1] <= w:

            dp[i][w] = max(
                dp[i-1][w],
                profits[i-1] + dp[i-1][w - investments[i-1]]
            )

        else:
            dp[i][w] = dp[i-1][w]

max_profit = dp[n][budget]

selected = []
w = budget

for i in range(n, 0, -1):

    if dp[i][w] != dp[i-1][w]:

        selected.append(products[i-1])

        w -= investments[i-1]

selected.reverse()

print("Selected Products:", selected)

print("Maximum Profit =", max_profit)
