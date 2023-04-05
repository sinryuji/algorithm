import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  basket = input().rstrip()
  while '()' in basket:
        basket = basket.replace('()', '')
  if len(basket) > 0:
    print("NO")
  else:
    print("YES")