# 返回最小差距划分方法的最小差距，按行划分，传入二维数组
class Solution:
    def __init__(self, mat = None):
        if mat is None:
            self._input()
        else:
            self.mat = mat
            self.n = len(mat)
            self.m = len(mat[0])
    
    def _input(self):
        self.n, self.m = map(int, input().split())
        self.mat = []
        for _ in range(self.n):
            self.mat.append(list(map(int, input().split())))
    
    def get_prefix_row_mat(self):
        prefix_row_mat = [[0] * self.m for _ in range(self.n)]
        prefix_row_mat[0] = self.mat[0]
        for i in range(1, self.n):
            for j in range(self.m):
                prefix_row_mat[i][j] = prefix_row_mat[i - 1][j] + self.mat[i][j]
        return prefix_row_mat
    
    def get_prefix_row_list(self):
        prefix_row_mat = self.get_prefix_row_mat()
        prefix_row_list = []
        for i in range(self.n):
            prefix_row_list.append(sum(prefix_row_mat[i]))
        return prefix_row_list
    
    def get_row_min_gap(self):
        prefix_row_list = self.get_prefix_row_list()
        min_gap = prefix_row_list[-1]
        for i in range(self.n):
            cur_gap = abs(2 * prefix_row_list[i] - prefix_row_list[-1])
            min_gap = min_gap if min_gap < cur_gap else cur_gap
        return min_gap
    
    def get_transpose_mat(self):
        tmat = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                tmat[i][j] = self.mat[j][i]
        return tmat

def main():
    solution_row = Solution()
    min_gap_row = solution_row.get_row_min_gap()
    solution_col = Solution(solution_row.get_transpose_mat())
    min_gap_col = solution_col.get_row_min_gap()
    ans = min(min_gap_col, min_gap_row)
    return ans

if __name__ == "__main__":
    print(main())