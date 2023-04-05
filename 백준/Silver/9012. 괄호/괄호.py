import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  basket = list(input())
  cnt = 0
  while len(basket) > 0:
    c = basket.pop()
    if c == ')':
      cnt += 1
    elif c == '(':
      cnt -= 1
    if cnt < 0:
      print("NO")
      break
  if cnt == 0:
    print("YES")
  elif cnt > 0:
    print("NO")