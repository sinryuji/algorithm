import sys
input = sys.stdin.readline

def is_basket(c):
  if c == '(':
    return True
  if c == ')':
    return True
  if c == '[':
    return True
  if c == ']':
    return True
  return False

while True:
    str = input().rstrip()
    if str == ".":
        break
    for c in str:
      if is_basket(c) == False:
        str = str.replace(c, '')
    while '()' in str or '[]' in str:
        str = str.replace('()', '')
        str = str.replace('[]', '')
    if len(str) == 0:
        print('yes')
    else:
        print('no')