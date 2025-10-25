number = int(input())
A = []
count = 0
A += input()
for i in range(number-1):
    if A[i] == A[i+1]:
        count += 1
print(count)
