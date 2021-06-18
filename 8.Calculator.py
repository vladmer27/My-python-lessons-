# *** пример калькулятор 

# функция обработчик 
def calculate(n1, n2, op):
    if op == "+":
        result = n1 + n2 
    elif op == "/":
        result = n1 / n2
    elif op == '-':
        result = n1 - n2 
    elif op == '*':
        result = n1 * n2 
    else: 
        result = f"что это такое: {op}?"
    return result  

#цикл программ 
while True:
    # ввод данных 
    cmd = input("комундайте сэр!")
    if cmd == "stop":
        print("buy buy!")
        break 
    
    num_1 = int(input("Введите первое число:"))
    num_2 = int(input("Введите второе число:"))
    op = input("введите символ операции: ")

    # обработка данных
    result = calculate(num_1, num_2, op)

    # вывод данных 
    print(f'результат: {result}')