import sys

sys.stdin.readline()
a = set(sys.stdin.readline().split())
sys.stdin.readline()
sys.stdout.write('\n'.join('1' if i in a else '0' for i in sys.stdin.readline().split()))