pattern = input()
text = input()
c = int(input())

for i in range(len(text) - len(pattern) + 1):
    sub_str = text[i:i + len(pattern)]
    count = 0

    for j in range(len(pattern)):
        if pattern[j] != sub_str[j]:
            count += 1

    if count <= c:
        print(i)
