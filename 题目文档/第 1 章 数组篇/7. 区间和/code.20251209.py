n = int(input())
prefix_sum = [int(input())]
for i in range(1, n):
    prefix_sum.append(prefix_sum[i - 1] + int(input()))
while True:
    try:
        l, r = map(int, input().split())
    except:
        break
    if l == 0:
        print(prefix_sum[r])
    else:
        print(prefix_sum[r] - prefix_sum[l - 1])