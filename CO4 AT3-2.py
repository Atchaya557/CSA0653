# Atchaya Vharsne S (192524185)
packages = [
    ("P1", 10, 60),
    ("P2", 20, 100),
    ("P3", 30, 120),
    ("P4", 25, 110)
]
capacity = 50
packages.sort(key=lambda x: x[2]/x[1], reverse=True)
selected = []
total_weight = 0
total_profit = 0
for name, weight, profit in packages:
    if total_weight + weight <= capacity:
        selected.append(name)
        total_weight += weight
        total_profit += profit
print("Selected Packages:", selected)
print("Total Weight:", total_weight)
print("Total Profit:", total_profit)

# Dynamic
packages = [
    ("P1", 10, 60),
    ("P2", 20, 100),
    ("P3", 30, 120),
    ("P4", 25, 110)
]
capacity = 50
weights = [10, 20, 30, 25]
profits = [60, 100, 120, 110]
names = ["P1", "P2", "P3", "P4"]
n = len(weights)
dp = [[0]*(capacity+1) for _ in range(n+1)]
for i in range(1, n+1):
    for w in range(capacity+1):
        if weights[i-1] <= w:
            dp[i][w] = max(
                profits[i-1] + dp[i-1][w-weights[i-1]],
                dp[i-1][w]
            )
        else:
            dp[i][w] = dp[i-1][w]
w = capacity
selected = []
for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
        selected.append(names[i-1])
        w -= weights[i-1]
selected.reverse()
print("Selected Packages:", selected)

print("Maximum Profit:", dp[n][capacity])
