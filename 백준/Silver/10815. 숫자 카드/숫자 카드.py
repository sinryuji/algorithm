import sys

sys.stdin.readline()
cards = set(sys.stdin.readline().split())
sys.stdin.readline()
sys.stdout.write(" ".join(["1" if i in cards else "0" for i in sys.stdin.readline().split()]))