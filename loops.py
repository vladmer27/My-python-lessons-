# * * * ЦИКЛЫ * * *

# оператор цикла While

# БЕСКОНЕЧНЫЙ ЦИКЛ
# while True:
#     print("hello")

# I = 1
# while I <= 2: 
#     print(I**2)
#     I = I +1

g = 10
while g > 0:
    g -= 1
    print (f"hello {g}")

# инструкция прерывания цикла по доп. условию
# g = 10
# while g > 0:
#     print (f"hello {g}")
#     if g == 5:
#         break
#     g -= 1
    
# *** Оператор цикла for *** 
# 1. Читает значение itaruable (list, tuple, string) по порядку
# 2. значение присваивает в свою переменную 
# 3. Выполняет блок кода своего тела 

my_list = [10,20,30,40,50,60,70]
my_list.remove(10)
print(my_list)
for i in my_list[::-1]:
    print(i)

# генератор списка 
# создание листа чисел в диапозоне от 10 до 100 с шагом 10
# num_list = [num *2 for num in range(10, 100, 10)]
# print(num_list)


