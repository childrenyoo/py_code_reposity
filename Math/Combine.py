#计算组合数
import math
def Combine(m,n):
    if n>m:
        return 0
    if n>m-n:
        res=getln(m,n+1)
        res-=getln(m-n,1)
    else:
        res=getln(m,m-n+1)
        res-=getln(n,1)
    return round(math.exp(res))

#计算ln(max)+ln(max-1)+……+ln(min)
def getln(max,min):
    res=0
    for i in range(min,max+1):
        res+=math.log(i)
    return res