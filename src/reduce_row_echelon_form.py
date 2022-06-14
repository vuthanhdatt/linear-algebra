# Pseudocode:
# function ToReducedRowEchelonForm(Matrix M) is
#     lead:= 0
#     rowCount:= the number of rows in M
#     columnCount:= the number of columns in M
#     for 0 ≤ r < rowCount do
#         if columnCount ≤ lead then
#             stop function
#         end if
#         i = r
#         while M[i, lead] = 0 do
#             i = i + 1
#             if rowCount = i then
#                 i = r
#                 lead = lead + 1
#                 if columnCount = lead then
#                     stop function
#                 end if
#             end if
#         end while
#         if i ≠ r then Swap rows i and r
#         Divide row r by M[r, lead]
#         for 0 ≤ i < rowCount do
#             if i ≠ r do
#                 Subtract M[i, lead] multiplied by row r from row i
#             end if
#         end for
#         lead = lead + 1
#     end for
# end function


def reduce_row_echelon_form(A):
    """
    Function that reduces a matrix to row echelon form.
    """
    lead = 0
    rowCount = len(A)
    columnCount = len(A[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return A
        i = r
        while A[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return A
        if i != r:
            A[i], A[r] = A[r], A[i]
        pivot = A[r][lead]
        for j in range(columnCount):
            A[r][j] = A[r][j] / pivot
        for i in range(rowCount):
            if i != r:
                t = A[i][lead]
                for j in range(columnCount):
                    A[i][j] = A[i][j] - t * A[r][j]
        lead += 1

if __name__ == '__main__':
    A = [[1,2,3],[4,5,6],[7,8,9]]
    print(reduce_row_echelon_form(A))