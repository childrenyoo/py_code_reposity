#题目：实现一个函数用来匹配包含"."和"*"的正则表达式。
# "."表示任意一格字符；"*"表示它前面的字符可以出现任意次（包括0次）
#如“aaa”与“a.a”和“ab*aca”匹配，与“aa.a”和“ab*a”不匹配

def match(s,pattern):
    if s=='' or pattern=='':
        return False

def matchCore(s,pattern):
    if s==''and pattern=='':
        return True
    if s!=''and pattern=='':
        return False
    if pattern[1]=="*":
        if pattern[0]==s[0] or (pattern[0]=='.'and s[0]!=''):
            return