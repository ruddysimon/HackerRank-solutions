if __name__ == '__main__':
    n = int(input())
    dic = {}
    for i in range(n):
        arr = score,*line = input().split()
        name = arr[0]
        # print(name)
        scores = list(map(float,line))
        # print(scores)
        average_score = sum(scores) / float(len(scores))
        # print(average_score)
        dic[score] = average_score 
    name = input()
print('%.2f'% dic[name])