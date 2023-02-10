import sys

l = sys.stdin.readlines()[1:]
l.sort(key=lambda x: int(x.split()[1]))
l.sort(key=lambda x: int(x.split()[0]))
sys.stdout.write(''.join(l))