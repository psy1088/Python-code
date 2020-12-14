# 이차원 행렬 시계방향으로 90도 회전
def rotation_matrix_90degree(x):
    row = len(x)
    col = len(x[0])
    trans_arr = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            trans_arr[i][j] = x[row - 1 - j][i]
    return trans_arr
