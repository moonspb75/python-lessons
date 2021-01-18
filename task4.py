n=int(input())
maxn=0
while n > 10:
    if (n % 10)> maxn:
        maxn= n % 10
    n=n//10
if (n % 10)> maxn:
    maxn= n % 10
print(maxn)