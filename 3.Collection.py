# ***Коллекция (контейнеры)***

#  ***список (list)***
# созданеи пустого списка
# my_list = (1, [2,3],4)
# print (my_list)
# my list [] = list(1,2,3,4)...


my_list = []
my_list = list ()

# PEP8 
# добавление объекта (элемента) в список
my_list.append(100)
my_list.append(3.14)
my_list.append("hello")
my_list.append([10,20,30,40])

# .append несамостоятельная функция только для списка
# print (my_list)

# чтение значений элемента
# индексирование my_list.append([10,20,30,40]) = 10 = 0, 20=1 30=2
el = my_list[3]
el = my_list[3][2]
print(el)

# обратная индексация 
el = my_list[-1]

# замена значения элемента 
my_list[0] = 2000

# удаление элемента по значению 
# my_list.remove(3.14)

# удаление элемента по индексу 
del my_list[-1]
print (my_list)

# срез списка 
s= "hello world"
my_list =  list(s)

my_slice = my_list[2:]
my_slice = my_list[2:5]
print(my_slice)
# git addd . 
# git commit -m "message"
# git push

