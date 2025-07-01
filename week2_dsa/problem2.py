#total number of units of memory after processing the requests
server1_sum = 0
server2_sum = 0
N = int(input('Enter the number of requests: '))
requests = input('Enter the elements: ').split()
for i in range(N):
    if i%2 == 0:
        server1_sum += int(requests[i])
    else:
        server2_sum += int(requests[i])
print('Total units of memory allocated/deallocated for server 1: ', server1_sum)