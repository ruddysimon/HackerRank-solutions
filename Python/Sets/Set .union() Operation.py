n = int(input())
N = set([int(i) for i in input().split()])
m = int(input())
M = set([int(i) for i in input().split()])
union_integers = M.union(N)
print(len(union_integers))