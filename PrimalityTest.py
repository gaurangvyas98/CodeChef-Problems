def prime(no):
    if no<2:
        return 0
    for i in range(2,no):
        if no%i==0:
            return 0
    return 1


n = int(input())
for i in range(n):
    p = int(input())
    if prime(p)==1:
        print("yes")
    else:
        print("no")