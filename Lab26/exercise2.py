class Stackoverflow(Exception):
    pass
class Stackunderflow(Exception):
    pass


class Stacks:
    def __init__(self, cap):
        self.s = []
        self.max_size = cap

    def push(self,val):
        if len(self.s) > self.max_size:
            raise Stackoverflow('capacity full, cannot perform push')
        self.s.append(val)

    def pop(self):
        if len(self.s) == 0:
            raise Stackunderflow('stack empty, cannot pop empty stack')
        x = self.s.pop()
        return x

    def peek(self):
        # return len(self.s)-1 #will return index
        return self.s[-1]

    def traversal(self):
        return self.s[::-1]




st = Stacks(4)
st.push(5)
st.push(6)
st.push(7)
st.push(9)
print(st.s)
st.pop()
print(st.s)
print(st.peek())
print(st.traversal())











