import sys

data = sys.stdin.readlines()[1:]
data.sort(key = lambda x: int(x.split()[0]))
sys.stdout.write("".join(data))