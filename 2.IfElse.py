#***Logic operations*** 

# z= 3
# W=2 

#операция СРАВНЕНИЯ 

# операция "равно"
# мы спрашиваем "значение z равно значению W?"
#результат будет присвоен переменной result 
# result = z == W
# print(result)g

# #операция "не равно"
# result = z!=W
# print (result)

# #операция "меньше"
# result = z < W
# print(result)

# #оерация "больше"
# result = z>W
# print(result)

# #операция "меньше или равно"
# result = z<=W
# print(result)

# #операция "больше или равно"
# result = z>=W
# print(result)

#Логические операции

# var_1 = True
# var_2 = True 

# #оператор "НЕ" (NOT)
# result = not var_1
# print(result)

# #оператор "И" (AND) = возвращает только тогда, 
# # когда обе переменных являются True, во всех остальных случаях 
# # будет false 

# result = var_1 and var_2
# print(result)

# #оператор "Или (OR)"
# #Возвращает False только тогда, 
# # когда обе переменных False 
# result = var_1 or var_2
# print(result)

#*** условные операторы*** 
#оператор if ("если")
# if False:
#     W = "hello"
#     print(W)

# Z = 10
# if Z < 3:
#     print("меньше")
# else:
#     print("не меньше")

V = 'C'
if V == 'B':
    result = 'literal B'
elif V== 'A':
    result = 'literal A'
elif V== 'D':
    result = 'literal D'
elif V== 'C':
    result = 'literal C'
else: 
    result = 'непонятный символ'

# print (result)

#чтобы сохранить файл в терминале: git add. 
#git commit - m "создан файл 2.ifelse.py"
#git push
