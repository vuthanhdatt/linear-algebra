

def matrix_multiply(A,B):
    m = len(A)
    k = len(B[0])
    n = len(B)
    result = [[0]*k for _ in range(m)]
    for i in range(m):
        for j in range(k):
            for l in range(n):
                result[i][j] += A[i][l] *B[l][j]
    return result

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    B = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix_multiply(A,B))