import sys

sys.stdin.readline()
sys.stdout.write("".join(sorted(list(set(sys.stdin.readlines())), key = lambda x: (len(x), x))))