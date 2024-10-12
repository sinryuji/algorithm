N = input()

left = sum(list(map(int, N[:len(N)//2])))
right = sum(list(map(int, N[len(N)//2:])))

if left == right:
    print("LUCKY")
else:
    print("READY")