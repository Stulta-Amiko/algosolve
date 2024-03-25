a,b,c = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[a-1]
second = data[a-2]

total = 0

maxproduct = b // (c+1)
secondproduct = b % (c+1)

total += first * maxproduct * (c+secondproduct)
total += second * maxproduct

print(total)

# 큰 수의 법칙 