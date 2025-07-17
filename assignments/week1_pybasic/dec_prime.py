#Print the Prime numbers in decreasing order between m and n (m < n)
m = int(input('Enter the First number m: '))
n = int(input('Enter the Second number n: '))
if m < n:
    prime_list = []
    for i in range(n,m,-1):
        if i > 2:
            for j in range(2,i):
                if i%j == 0:
                    break
            else:
                prime_list.append(i)
        elif i == 2:
            prime_list.append(i)
print('The Decreasing order of Prime numbers is:',prime_list)