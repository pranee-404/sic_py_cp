#Find smallest of 3 distinct numbers
a,b,c = input('Enter Three Numbers:').split()
a = int(a)
b = int(b)
c = int(c)
if a < b and a < c:
    print(a, 'is the Smallest Number')
elif b < a and b < c:
    print(b, 'is the Smallest Number')
else:
    print(c, 'is the Smallest Number')