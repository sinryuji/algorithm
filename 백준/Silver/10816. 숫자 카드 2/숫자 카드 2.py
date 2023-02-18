import sys
from collections import Counter

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
c = Counter(cards)
sys.stdout.write((' '.join([str(c[int(i)]) if int(i) in c else "0" for i in sys.stdin.readline().split()])))