x,n=map(int,input().split())
p=(n-(x*100))/100
if(p-int(p))>0:
    print(int(p)+1)
else:
    print(int(p))
