# Задача №24
n = list(map(int, input().split()))
summax = 0
for i in range(len(n)):
    sum = n[i-2]+n[i]+n[i-1]
    if sum > summax:
        summax = sum    
print(summax)