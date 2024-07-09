N = int(input())
people = list(map(int, input().split()))
T, P = map(int, input().split())

print(sum([(n - 1) // T + 1 for n in people]))
print(N // P, N % P)