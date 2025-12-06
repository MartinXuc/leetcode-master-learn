s = input()
s = list(s)
for i, c in enumerate(s):
    if c.isdigit():
        s[i] = "number"
print("".join(s))