name = input()

characters = dict()
for char in name:
    characters.setdefault(char, 0)
    characters[char] += 1
        
answer, odd_char = '', ''
for char, cnt in sorted(characters.items()):
    if cnt % 2:
        if odd_char != '':
            print("I'm Sorry Hansoo")
            break
        odd_char = char
    answer += char * (cnt // 2)
else:
    print(answer + odd_char + answer[::-1])