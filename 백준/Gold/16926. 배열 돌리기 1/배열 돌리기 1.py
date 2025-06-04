import sys

input = sys.stdin.readline

def get_layer_coords(layer):
    coords = []

    coords += [(layer, j) for j in range(layer, M - 1 - layer)]
    coords += [(i, M - 1 - layer) for i in range(layer, N - 1 - layer)]
    coords += [(N - 1 - layer, j) for j in range(M - 1 - layer, layer, -1)]
    coords += [(i, layer) for i in range(N - 1 - layer, layer, -1)]

    return coords

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

layers = min(N, M) // 2
for layer in range(layers):
    coords = get_layer_coords(layer)
    values = [arr[i][j] for i, j in coords]
    for _ in range(R):
        values.append(values.pop(0))
    for (i, j), val in zip(coords, values):
        arr[i][j] = val

for i in range(N):
    print(*arr[i])
