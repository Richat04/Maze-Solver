class Stack:
    def __init__(self) -> None:
        self.create_stack=[]
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
    def push(self, x, y):
        a=(x,y)
        self.create_stack.append(a)
        pass
    def pop_ele(self):
        self.create_stack.pop()
    def is_empty(self):
        if len(self.create_stack)==0:
            return True
        else:
            return False
    def is_in(self, x, y):
        ans=False
        for i in self.create_stack:
            if i[0]==x and i[1]==y:
                ans=True
        return ans
    def length(self):
        c=0
        for i in self.create_stack:
            c=c+1
        return c
    def return_last(self):
        a=0
        for i in self.create_stack:
            a=i
        return a
    def print_stack(self):
        l=[]
        for i in self.create_stack:
            l.append(i)
        return l
    # You can implement this class however you like