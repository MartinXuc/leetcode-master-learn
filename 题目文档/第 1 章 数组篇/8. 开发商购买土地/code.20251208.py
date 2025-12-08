n, m = map(int, input().split())
mat = []

# 读取矩阵
for i in range(n):
    mat.append(list(map(int, input().split())))

# 求按行划分前缀和
def min_row_gap(mat):
    n = len(mat)
    prefix_row_sum = [sum(mat[0])]
    for i in range(1, n):
        prefix_row_sum.append(prefix_row_sum[i - 1] + sum(mat[i]))

    all_sum = prefix_row_sum[n - 1]
    min_gap = all_sum

    # 求差值
    for i in range(n):
        gap = abs(all_sum - 2 * prefix_row_sum[i])
        min_gap = min(min_gap, gap)
    
    return min_gap

# 求按列划分的前缀和
def min_col_gap(mat):
    n = len(mat)
    m = len(mat[0])
    # 求转置矩阵
    mat_t = [[0] * n for _ in range (m)]
    for i in range(n):
        for j in range(m):
            mat_t[j][i] = mat[i][j]
    return min_row_gap(mat_t)

print(min(min_row_gap(mat), min_col_gap(mat)))