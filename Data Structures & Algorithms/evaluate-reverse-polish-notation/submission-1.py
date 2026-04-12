class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack for the numbers 
        # whenever we reach an operator, do it to everything in the stack. 
        # push result back into stack 

        stack = []

        for token in tokens:
            if token == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2 - num1)
            elif token == '*':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(num1) * int(num2))            
            elif token == '/':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(int(num2) / int(num1)))
            # has to be a number
            else:
                stack.append(int(token))
        
        return stack[0]
        