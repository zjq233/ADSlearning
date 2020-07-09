#定义栈类,栈 后进先出,先进后出
class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items == []

    def push(self,item):  #进栈
        self.items.append(item)

    def pop(self): #出栈
        return self.items.pop()

    def peek(self): #返回栈顶数据项
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

