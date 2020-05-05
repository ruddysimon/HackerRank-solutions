if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    largest_num = max(arr)
    for i in range(n):
        if largest_num == max(arr):
            arr.remove(max(arr))
    print(max(arr))