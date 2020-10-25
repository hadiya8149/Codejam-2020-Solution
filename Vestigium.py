T = int(input())
for i in range(T):
    matrix = []
    matrix_size = int(input())
    for l in range(0, matrix_size):
        m1list = list(map(int, input().strip().split()))[:matrix_size]
        matrix.append(m1list)
# where k  is the sum of the diagonal entries from top left to top right


    def diagonal_sum(matrix, matrix_size):
        sum_matrix = 0
        for e in range(0, matrix_size):
            sum_matrix += matrix[e][e]
        return sum_matrix

    diag_sum = diagonal_sum(matrix, matrix_size)
# no of repetitions in a column


    def row_rep(matrix, matrix_size):
        rep = 0
        for i in range(0, matrix_size):
            for element in matrix[i]:
                if matrix[i].count(element) > 1:
                    rep += 1
                    break
        return rep


    def col_rep(matrix, matrix_size):
        rep = 0
        col_matrix = [[matrix[c][r] for c in range(len(matrix))] for r in range(len(matrix[0]))]
        for k in range(0, matrix_size):
            for element in col_matrix[k]:
                if col_matrix[k].count(element) > 1:
                    rep += 1
                    break
        return rep

    row_counts = row_rep(matrix, matrix_size)
    col_counts = col_rep(matrix, matrix_size)
    #      Case #1: 4 0 0
    print("Case #{}: {} {} {}".format(i+1,str(diag_sum),str(row_counts),str(col_counts)))