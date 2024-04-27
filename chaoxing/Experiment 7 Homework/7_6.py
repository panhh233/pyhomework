def count_possible_weights(n, weights, quantities):
    max_weight = sum(weights[i] * quantities[i] for i in range(n))

    dp = [False] * (max_weight + 1)
    dp[0] = True  

    for i in range(n):
        weight = weights[i]
        quantity = quantities[i]

        for j in range(max_weight, weight - 1, -1):
            for k in range(1, min(quantity, j // weight) + 1):
                if dp[j - k * weight]:
                    dp[j] = True
                    break

    return sum(dp)

n = int(input())
weights = list(eval(input()))
quantities = list(eval(input()))

result = count_possible_weights(n, weights, quantities)
print(result)