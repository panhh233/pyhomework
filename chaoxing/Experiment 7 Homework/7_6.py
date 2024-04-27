def count_possible_weights(n, weights, quantities):
    # 确定最大可能的重量
    max_weight = sum(weights[i] * quantities[i] for i in range(n))

    # 初始化dp数组，长度为最大重量+1
    dp = [False] * (max_weight + 1)
    dp[0] = True  # 不使用任何砝码的情况

    # 遍历每种砝码
    for i in range(n):
        weight = weights[i]
        quantity = quantities[i]

        # 采用多重背包的处理方式，这里我们从大到小遍历防止重复使用砝码
        for j in range(max_weight, weight - 1, -1):
            # 尝试使用从1到quantity个砝码，看能否到达j重量
            for k in range(1, min(quantity, j // weight) + 1):
                if dp[j - k * weight]:
                    dp[j] = True
                    break

    # 计算dp中True的数量，即不同的可达重量
    return sum(dp)


# 示例输入
n = 3
weights = [1, 2, 5]
quantities = [1, 1, 1]

# 输出结果
result = count_possible_weights(n, weights, quantities)
print(result)