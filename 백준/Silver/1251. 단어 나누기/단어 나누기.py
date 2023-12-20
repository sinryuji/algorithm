word = input()
word_len = len(word)
answer = "z" * word_len

for i in range(1, word_len - 1):
    for j in range(i + 1, word_len):
        first = word[0:i]
        second = word[i:j]
        third = word[j:]
        tmp = first[::-1] + second[::-1] + third[::-1]
        if answer > tmp:
            answer = tmp

print(answer)