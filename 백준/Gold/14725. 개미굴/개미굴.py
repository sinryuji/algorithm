import sys

input = sys.stdin.readline

class Trie:
    def __init__(self):
        self.root = {}
        
    def insert(self, foods):
        cur = self.root
        
        for food in foods:
            if food not in cur:
                cur[food] = {}
            cur = cur[food]
        
        cur[0] = True
        
    def search(self, level, cur):
        if 0 in cur:
            return
        cur_child = sorted(cur)
        
        for ch in cur_child:
            print("--" * level + ch)
            self.search(level + 1, cur[ch])

N = int(input())
trie = Trie()
for _ in range(N):
    trie.insert(list(input().split())[1:])

trie.search(0, trie.root)
    