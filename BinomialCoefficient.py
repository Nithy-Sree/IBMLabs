def bincoef(n,k):
    C = [[0 for i in range(n+1)] for j in range(n+1)]
    for row in range(n+1):
        for col in range(min(row, k)+1):
            if col==0 or col==row:
                C[row][col] = 1
            else:
                C[row][col] = C[row-1][col-1] + C[row-1][col]
    return C[n][k]

n,k = map(int,input().split())
print(bincoef(n,k))
