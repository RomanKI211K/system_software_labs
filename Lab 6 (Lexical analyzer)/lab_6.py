import random
import re

# Список ключових слів і символів мови
keywords = ['if', 'then', 'else']
operators = ['+', '-', '*', '/', '>', '<', '=', ':=']
delimiters = ['(', ')', '{', '}', ',', ';']
comparators = ['<', '>', '=']

# Відкриття файлу з вхідним текстом для читання
with open('input.txt', 'r') as file:
    # Читання вхідного тексту
    data = file.read()

# Розбиття вхідного тексту на лексеми
tokens = re.findall('\w+|[%s]|[%s]|[%s]|[\d]+|\S' % ('|'.join(operators), '|'.join(delimiters), '|'.join(comparators)), data)

# Список лексем
lexemes = []

# Проходження через список лексем та визначення їх типів
for token in tokens:
    # Лексема є ключовим словом
    if token in keywords:
        lexemes.append(('Keyword', token))
    # Лексема є оператором
    elif token in operators:
        lexemes.append(('Operator', token))
    # Лексема є роздільником
    elif token in delimiters:
        lexemes.append(('Delimiter', token))
    # Лексема є порівняльним оператором
    elif token in comparators:
        lexemes.append(('Comparator', token))
    # Лексема є цілим числом
    elif token.isdigit():
        lexemes.append(('Integer', int(token)))
    # Лексема є римським числом
    elif re.match('(M|MM|MMM)?(C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?(X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?(I|II|III|IV|V|VI|VII|VIII|IX)?', token):
        lexemes.append(('Roman Numeral', token))
    # Лексема є ідентифікатором
    elif re.match('[a-zA-Z]{1}[a-zA-Z0-9]{0,31}', token):
        lexemes.append(('Identifier', token))
    # Лексема є рядковою константою
    elif re.match('"[^\n"]{0,32}"', token):
        lexemes.append(('String', token[1:-1]))
    # Лексема є недопустимим символом
    else:
        print('Error: Invalid token - %s' % token)
        lexemes.append(('Invalid Token', token))

# Виведення таблиці лексем з вказівкою їх типів та значень
print('Token\t\t\tType\t\tValue')
print('--------------------------------------------')
for lexeme in lexemes:
    print('{:<20}{:<20}{}'.format(lexeme[1], lexeme[0], lexeme[1]))
