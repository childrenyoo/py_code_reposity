#数据结构：栈的实现
#未完成
class stack:
    def __init__(self):
        self.list = []
        self.top = 0
    def push(self,x):
        self.list.append(x)

    def pop(self):
        if len(self.list)>0:
            res=self.list[-1]
            del self.list[-1]
            return res
        else:
            return "stack is empty"

    def top(self):
        if len(self.list)>0:
            return self.list[-1]
        else:
            return "stack is empty"
