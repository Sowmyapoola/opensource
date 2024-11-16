def fact(N):
    if N==0:
        return 1
    else:
        return N* fact(N-1)
N=int(input())
print(fact(N))
