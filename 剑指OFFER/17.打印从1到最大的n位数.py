#题目：输入数字n，按顺序打印出从1到最大的n位十进制数，n=3时，打印1~99
#注意n可能很大
def printToNDigits(n):
    s="0"*n
    s=addOne(s)
    max="9"*n
    while s!=max:
        printS(s)
        s=addOne(s)
    printS(max)

#给s代表的数字加1
def addOne(s):
    for i in  range(len(s)-1,-1,-1):
        if s[i]!="9":
            tmp=str(int(s[i])+1)
            s=s[:i]+tmp+s[i+1:]
            break
        else:
            s=s[:i]+"0"+s[i+1:]
            if i==0:
                s="1"+s
    return s

#打印s,去除前面的0
def printS(s):
    start=0
    for i in range(len(s)):
        if s[i]=="0":
            start+=1
        else:
            break
    print(s[start:])
printToNDigits(4)