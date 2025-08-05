s = input()
s_list = list(s)
number_count = 0
for char in s:
    if ord(char) in range(ord('0'), ord('9') + 1):
        number_count += 1
s_list.extend(['0'] * 5 * number_count)
l = len(s) - 1
r = len(s_list) - 1
while l >= 0:
    if ord(s_list[l]) in range(ord('0'), ord('9') + 1):
        s_list[r] = 'r'
        r -= 1
        s_list[r] = 'e'
        r -= 1
        s_list[r] = 'b'
        r -= 1
        s_list[r] = 'm'
        r -= 1
        s_list[r] = 'u'
        r -= 1
        s_list[r] = 'n'
    else:
        s_list[r] = s_list[l]
    l -= 1
    r -= 1
print("".join(s_list))