s = input()
s_list = list(s)
for index, char in enumerate(s_list):
    if ord(char) in range(ord('0'), ord('9') + 1):
        s_list[index] = "number"
print("".join(s_list))