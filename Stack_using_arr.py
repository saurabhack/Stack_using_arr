def create_stack():
    stack=[]
    return stack
def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
def pop(stack):
    if isempty(stack):
        return "stack is already empty"
    stack.pop()

def peek(stack):
    size=len(stack)
    top=stack[size-1]
    return top
def display(stack):
    size=len(stack)
    for i in range(size):
        print(stack[i],end=" ")

stack=create_stack()
push(stack,int(1))
push(stack,int(2))
push(stack,int(3))
display(stack)
print("\nthe top element from the stack is =",peek(stack))
pop(stack)
display(stack)
print("\nthe top element from the stack is =",peek(stack))