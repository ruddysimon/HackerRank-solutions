names_scores = []
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores += [[name,score]]
        scorelist += [score]
    a = sorted(set(scorelist))[1]
    # print(a) ''desregard this line, i'm debugging step by step by printing''
    i = name
    j = score
    for i, j in sorted(names_scores):
        if j == a:
            print(i)