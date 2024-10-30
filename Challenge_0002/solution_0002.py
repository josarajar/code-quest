M = [[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]

i1 = 1
j1 = 2
i2 = 2
j2 = 3

result = 0
nops = 0
for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] < M[i1][j1] or M[i][j] > M[i2][j2]:
            result+=1
        nops+=1
print(f'Full computation number of ops: {nops}. Result: {result}')

result=0
nops = 0

# Count rows smaller than i1
for i in range(i1):
    for j in range(len(M[i])):
        nops+=1
        print(M[i][j])
        if M[i][j] >= M[i1][j1]:
            result+=j
            print(f'subresult: {j}')
            break
        elif j==len(M[i]):
            result+=len(M[i])
            print(f'subresult: {len(M[i])}')
# Count columns smaller than j1
for j in range(j1):
    for i in range(i1+1, len(M)):
        nops+=1
        print(M[i][j])
        if M[i][j] >= M[i1][j1]:
            result+=i-i1
            print(f'subresult: {i-i1}')
            break
        elif i==len(M)-1:
            result+=len(M)-i1
            print(f'subresult: {len(M)-i1}')
# Count rows greater than i2
for i in range(i2+1, len(M)):
    for j in reversed(range(len(M[i]))):
        nops+=1
        print(M[i][j])
        if M[i][j] <= M[i2][j2]:
            result+=(len(M[i])-j-1)
            print(f'subresult: {(len(M[i])-j-1)}')
            break
        elif j==0:
            result+=len(M[i])
            print(f'subresult: {len(M[i])}')

# Count columns greater than j2
for j in range(j2+1, len(M[0])):
    for i in reversed(range(i2)):
        nops+=1
        print(M[i][j])
        if M[i][j] <= M[i2][j2]:
            result+=(len(M)-i-i2-1)
            print(f'subresult: {(len(M)-i-i2-1)}')
            break
        elif i==0:
            result+=len(M)-i2
            print(f'subresult: {len(M)-i2}')

print(f'Reduced computation number of ops: {nops}. Result: {result}')
