import sys

# Функція для обчислення виразу
def calculate(expression):
    stack = []

    for char in expression:
        if char == '(':
            stack.append(char)
        elif char in ['+', '-']:
            stack.append(char)
        elif char == ')':
            temp = 0
            while stack[-1] != '(':
                operator = stack.pop()
                operand = int(stack.pop())
                if operator == '+':
                    temp += operand
                elif operator == '-':
                    temp -= operand
            stack.pop() # видаляємо відкриваючу дужку
            stack.append(str(temp)) # додаємо результат до стеку
        else: # символ є операндом
            stack.append(char)

    # Обчислюємо залишок стеку
    while len(stack) > 1:
        operator = stack.pop()
        operand = int(stack.pop())
        if operator == '+':
            stack[-1] = str(int(stack[-1]) + operand)
        elif operator == '-':
            stack[-1] = str(int(stack[-1]) - operand)

    return stack[0]

# Зчитуємо вхідний файл
input_file = sys.argv[1]
with open(input_file, 'r') as file:
    expression = file.read().strip()

# Обчислюємо вираз
result = calculate(expression)

# Записуємо результат у вихідний файл
output_file = input_file.split('.')[0] + '.res'
with open(output_file, 'w') as file:
    file.write(result)
