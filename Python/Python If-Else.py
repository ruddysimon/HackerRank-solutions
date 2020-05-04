n = int(input())
w = "Weird"
nw = "Not Weird"

# if n is odd
if n % 2 == 1:
    print(w)
# if n is even
else:
    if 2 <= n <= 5:
        print(nw)
    elif 6 <= n <= 20:
        print(w)
    elif n >= 20:
        print(nw)