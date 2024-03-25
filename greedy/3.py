a,b = map(int,input().split())
minmax = 0

for idx in range(a):
    data = list(map(int,input().split()))
    minValue = min(data)
    if minmax < minValue:
        minmax = minValue
    
print(minmax)

# 숫자 카드 게임
