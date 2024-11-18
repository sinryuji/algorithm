from itertools import combinations

def check(secret):
    cons, vowel = 0, 0
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    for c in secret:
        if c in vowel_list:
            vowel += 1
        else:
            cons += 1
        if cons >= 2 and vowel >= 1:
            return True
    return False

L, C = map(int, input().split())
letters = sorted(list(input().split()))

for secret in list(combinations(letters, L)):
    if check(secret):
        print(''.join(secret))
