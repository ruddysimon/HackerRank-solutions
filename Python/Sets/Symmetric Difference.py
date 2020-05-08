n = int(input())
M = set([int(i) for i in input().split()])
# print(M)
m = int(input())
N = set([int(i) for i in input().split()])
# print(N)
union_integers = M.union(N)
# print(union_integers)
inter_integers = M.intersection(N)
# print(inter_integers)
sym_difference = union_integers - inter_integers
list1 = [l for l in sym_difference]
list1.sort()
for i in list1:
    print(i)