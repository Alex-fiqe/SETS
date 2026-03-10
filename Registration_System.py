n=int(input())
m={}
for i in range(n):
    d=input()
    if(d not in m):
        m[d]=1
        print("OK")
    else:
        new=d+str(m[d])
        m[new]=1
        print(new)
        m[d]+=1
