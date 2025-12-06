n = int(input())
s = list(input())
if(n > len(s)):
    print("ValueError")
s1 = s[0:len(s) - n]
s2 = s[len(s) - n:]
print("".join(s2 + s1))