# prices = [100, 102, 98, 105, 103, 107, 99]


# for i in range(2, len(prices)):
#     total = prices[i]
#     for x in range(i-2, i):
#         total += prices[x]
        
#     print(total/3)

# prices = [100, 102, 98, 105, 103, 107, 99]

# window = 3
# total = sum(prices[:window])

# print(total / window)

# for i in range(window, len(prices)):
#     total += prices[i] - prices[i - window]
#     print(total / window)

def moving_average(prices, window):
    res = []
    total = sum(prices[:window])
    res.append(total/window)

    for i in range(window, len(prices)):
        total += prices[i] - prices[i - window]
        res.append(total/window)

    return res

prices = [100, 102, 98, 105, 103, 107, 99]
print(moving_average(prices, 3))
print(moving_average(prices, 5))