#题目实现函数power（double base，int exponent），求base的exponent此房，不得使用库函数，不考虑大树

#exponent为正数，负数，0；base为正数，负数，0
def power(base,exponent):
    if base==0:
        return 0
    if exponent==1:
        return base
    if exponent==0:
        return 1
    res=power(base,exponent>>1)
    res*=res
    if exponent&0x1==1:#奇数
        res*=base
    return res