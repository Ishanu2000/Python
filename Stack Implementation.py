#Represent a basic Stack
class Stack:
    def __init__(self):
        self.items = []  #List to hold stack elements

    #Push an item onto the stack
    def push(self, item):
        self.items.append(item)

    #Pop an item from the stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    #Check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0

    #Get the top item of the stack without removing it
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

#Check if a string of parentheses is balanced
def is_balanced_parentheses(expression):
    stack = Stack()
    #Dictionary to map opening to closing brackets
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in '({[':
            stack.push(char)  #Push opening brackets onto the stack
        elif char in ')}]':
            #Pop the top of the stack and check if it matches the current closing bracket
            if stack.is_empty() or stack.pop() != matching_bracket[char]:
                return False 
    
    #If the stack is empty after processing, parentheses are balanced
    return stack.is_empty()

#Example
e1 = "(([]){})"
e2 = "([)]"
e3 = "({[()]})"

print(f"Is '{e1}' balanced? {is_balanced_parentheses(e1)}")
print(f"Is '{e2}' balanced? {is_balanced_parentheses(e2)}")
print(f"Is '{e3}' balanced? {is_balanced_parentheses(e3)}")
