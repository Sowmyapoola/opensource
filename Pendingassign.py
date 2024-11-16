x,y,z=map(int,input().split())
tt=x*y
dtt=z*24*60
if(tt<=dtt):
    print('YES')
else:
    print('NO')
