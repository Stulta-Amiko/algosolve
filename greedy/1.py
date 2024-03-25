a = int(input())
total = 0
cointype = [500,100,50,10]

for coin in cointype:
    total += a // coin
    a %= coin

print(total)

# 거스름돈 
