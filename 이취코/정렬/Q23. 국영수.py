# https://www.acmicpc.net/problem/10825

import sys
input = sys.stdin.readline

def parse(line):
    name, kor, eng, math = line.split()
    kor, eng, math = int(kor), int(eng), int(math)
    return -kor, eng, -math, name

N = int(input())
score = [parse(input().rstrip()) for _ in range(N)]
print(*map(lambda x: x[3], sorted(score)), sep='\n')
