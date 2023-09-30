name = input()

characters = dict()
for char in name:
    if characters.get(char, 0) == 0:
        characters[char] = 1
    else:
        characters[char] += 1
        
keys = sorted(characters.keys())
odd_char = ""
for key in keys:
    if characters.get(key) % 2 == 1:
        if odd_char == "":
            odd_char = key
        else:
            print("I'm Sorry Hansoo")
            exit(0)

answer = ""
tmp = ""
for key in keys:
    tmp += key * (characters[key] // 2)
answer += tmp
answer += odd_char
answer += tmp[::-1]

print(answer)