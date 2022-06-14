
def row_echelon_form(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        all_zeros = True
        for j in range(n):
            if A[i][j] != 0:
                all_zeros = False
                break
        if all_zeros:
            temp = a[i]
            a[i] = a[m-1]
            a[m-1] = temp
            m -= 1
    
    p = 0
    while p < m and p < n:
        for i in range(p, m):
            if A[i][p] != 0:
                temp = A[i]
                A[i] = A[p]
                A[p] = temp
                break
        for i in range(p+1, m):
            if A[i][p] != 0:
                for j in range(p, n):
                    A[i][j] = A[i][j] - A[p][j] * (A[i][p] / A[p][p])
        p += 1
    return A

print(row_echelon_form([[1,3,-1], [0,1,7]]))