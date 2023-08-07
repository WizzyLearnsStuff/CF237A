n = int(input())

l = [0 for i in range(1440)]

for i in range(n):
    a, b = map(int, input().split())
    l[a * 60 + b] += 1

print(max(l))
