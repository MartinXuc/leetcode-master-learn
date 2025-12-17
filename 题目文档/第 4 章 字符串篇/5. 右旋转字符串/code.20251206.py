n = int(input())
s = input()
s_prefix = s[0:-n]
s_suffix = s[-n:]
print(s_suffix + s_prefix)