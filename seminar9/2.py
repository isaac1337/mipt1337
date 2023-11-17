class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            return "Неверное выражение"
        else:
            return self.items.pop()

def stack_calculator(expression):
    stack = Stack()
    symbols = expression.split()
    answer = 0

    for symbol in symbols:
        if symbol.isalnum():
            stack.add(symbol)
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()

            try:
                if symbol == '+':
                    answer = int(first_operand) + int(second_operand)
                elif symbol == '-':
                    answer = int(first_operand) - int(second_operand)
                elif symbol == '*':
                    answer = int(first_operand) * int(second_operand)
                elif symbol == '/':
                    answer = int(first_operand) / int(second_operand)
                elif symbol == '^':
                    answer = int(first_operand) ** int(second_operand)
                else:
                    raise ValueError("Неизвестный оператор")
                stack.add(answer)
            except (ValueError, ZeroDivisionError) as e:
                return "Ты втираешь мне какую-то дичь"

    return stack.pop()

expression = input()
print(stack_calculator(expression))
