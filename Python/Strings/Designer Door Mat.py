# First we are going to input our m and n which is 9, 27
n,m = map(int, input().split())

# We're consider this '.|.' as a string.
string1 = '.|.'

# For our middle part
string2 = 'WELCOME'

# Upper part
for i in range(n//2):
    print((string1 * ((i*2)+1)).center(m,'-'))

# Middle part
print(string2.center(m,'-'))

# Lower part
for i in range(n//2-1,-1,-1):
    print((string1 * ((i*2)+1)).center(m,'-'))