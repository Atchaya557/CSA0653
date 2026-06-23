#Atchaya Vharsne S (192524185)
investments = [("A", 20000, 25000),
    ("B", 30000, 40000),
    ("C", 40000, 50000),
    ("D", 50000, 70000)]
budget = 80000
investments.sort(key=lambda x: x[2] / x[1], reverse=True)
selected = []
total_capital = 0
total_return = 0
for name, capital, profit in investments:
    if total_capital + capital <= budget:
        selected.append(name)
        total_capital += capital
        total_return += profit
print("Selected Investments:", selected)
print("Total Capital Used:", total_capital)
print("Total Return:", total_return)
#dynamic
investments = [
    ("A", 20000, 25000),
    ("B", 30000, 40000),
    ("C", 40000, 50000),
    ("D", 50000, 70000)
]
budget = 80000
budget = budget // 10000
weights = [i[1] // 10000 for i in investments]
profits = [i[2] for i in investments]
names = [i[0] for i in investments]
n = len(investments)
dp = [[0]*(budget+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(budget+1):
        if weights[i-1] <= w:
            dp[i][w] = max(
                profits[i-1] + dp[i-1][w-weights[i-1]],
                dp[i-1][w]
            )
        else:
            dp[i][w] = dp[i-1][w]
w = budget
selected = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(names[i-1])
        w -= weights[i-1]
selected.reverse()
print("Selected Investments:", selected)
print("Maximum Return:", dp[n][budget])
