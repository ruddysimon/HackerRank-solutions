if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        x=name,*line = input().split()
        # print(x)
        command = x[0]
        if command == 'insert':
            list1.insert(int(x[1]),int(x[2]))
        if command == 'remove':
            list1.remove(int(x[1]))
        if command == 'append':
            list1.append(int(x[1]))
        if command == 'sort':
            list1.sort()
        if command == 'pop':
            list1.pop()
        if command == 'reverse':
            list1.reverse()
        if command == 'print':
            print(list1)

