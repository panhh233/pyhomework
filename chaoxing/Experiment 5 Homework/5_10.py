def isSymmetrical(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst[0])):
            if lst[i][j] != lst[j][i]:
                return False
    return True

def matrix_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i][i]
    return total

matrix = []

for i in range(4):
    row = input().strip().split(',')
    row = [int(num) for num in row]
    matrix.append(row)
if isSymmetrical(matrix):
    print("矩阵是对称矩阵")
else:
    print("矩阵不是对称矩阵")

diag_sum = matrix_sum(matrix)
print("矩阵对角线元素和是:", diag_sum)