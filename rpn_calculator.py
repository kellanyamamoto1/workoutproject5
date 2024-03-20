class RPNCalculator:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if len(self.stack) < 1:
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def add(self):
        b = self.pop()
        a = self.pop()
        self.push(a + b)

    def subtract(self):
        b = self.pop()
        a = self.pop()
        self.push(a - b)

    def multiply(self):
        b = self.pop()
        a = self.pop()
        self.push(a * b)

    def divide(self):
        b = self.pop()
        a = self.pop()
        self.push(a / b)

    def evaluate_rpn_expression(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit():
                self.push(int(token))
            elif token == '+':
                self.add()
            elif token == '-':
                self.subtract()
            elif token == '*':
                self.multiply()
            elif token == '/':
                self.divide()
            else:
                raise ValueError(f"Invalid token: {token}")

        return self.pop()
