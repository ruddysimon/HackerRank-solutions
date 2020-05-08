n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    x = name,*line = input().split()
    command = x[0]
    if command == 'pop':
        s.pop()
    if command == 'remove':
        s.remove(int(x[1]))
    if command == 'discard':
        s.discard(int(x[1]))
print(sum(s))
