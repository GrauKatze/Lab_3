def transpose(matrix):
    trans_matrix = [[0 for _ in range (len(matrix))] for _ in range(len(matrix[0]))]
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    matrix = trans_matrix