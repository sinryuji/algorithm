import sys

input = sys.stdin.readline


def compare_word(word1, word2):
    if len(word2) < len(word1):
        word1, word2 = word2, word1
    for c in word1:
        word2 = word2.replace(c, '', 1)
    if len(word2) > 1:
        return False
    return True

n = int(input())
word = input().rstrip()

ans = 0
for _ in range(n - 1):
    if compare_word(word, input().rstrip()):
        ans += 1

print(ans)