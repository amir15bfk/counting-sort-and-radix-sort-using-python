def counting_sort(A):
    k = max(A)+1
    l=[0]*(k)
    for i in A:
        l[i]+=1
    sum = 0
    for i in range(k):
        temp = l[i]
        l[i] = sum
        sum += temp
    output = [None]*(len(A))
    for i  in A:
        output[l[i]]=i
        l[i]+=1
    return output
def getdigit(num,n):
    r = num // pow(10, n)
    r = r % 10
    return r
def counting_sort_for_radix(A,n):
    k = 10
    l=[0]*(k)
    for i in A:
        l[getdigit(i,n)]+=1
    sum = 0
    for i in range(k):
        temp = l[i]
        l[i] = sum
        sum += temp
    output = [None]*(len(A))
    for i  in A:
        output[l[getdigit(i,n)]]=i
        l[getdigit(i,n)]+=1
    return output
def radix_sort(A):
    number = max(A)
    count = 0
    while (number > 0):
        number = number//10
        count = count + 1
    for n in range(count):
        A = counting_sort_for_radix(A,n)
        print(A)
    return A

A = [2341,1432,2413,1243,2143,1234]
out = radix_sort(A)
# print(out)