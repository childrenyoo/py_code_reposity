class queue:
    def __init__(self):
        self.list=[]

    def push(self,x):
        self.list.append(x)

    def pop(self):
        if len(self.list)>0:
            tmp=self.list[0]
            del self.list[0]
            return tmp
        else:
            return "queue is empty"