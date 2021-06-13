# s = "hello, world!"
# my_list = list(s)
# my_list.append(100)

# my_slice = my_list[2:]
# my_slice = my_list[2:5]
# my_slice = my_list[:5]
# # срез со 2-ого индекса до 12-ого не включительно 
# # с шагом 2
# my_slice = my_list[2:12:2]
# # обратная идексация 
# my_slice = my_list[-2:-5:-1]

# # переворот списка - в обратную сторону
# my_slice = my_list[::-1]

# print(my_list)
# print(my_slice)

# print(len(my_slice))
# print(len(my_list))

# dict 
# в паре ключ-значение
# {ключ_1: значение, ключ_2: значение}

my_dict = {'a':1.15, 'b':52.25, 'cba':3, 10:3.14} 
print(my_dict)
print(type(my_dict))
# чтение значений 
print(my_dict[10])
print(my_dict["cba"])

# Example 
data = {'name': 'Vladislav', 'age': 24, "ID": 123.5}
data1 = {'name': 'Jonh', 'age': 30, "ID": 12.5}
data2 = {'name': 'Misha', 'age': 25, "ID": 451}
total_data = {'p0':data, 'p1': data1, 'p2':data2}

print(total_data['p1']['name'])
print(total_data['p2']['name'])

# изменение значений 
my_dict['cba'] = 'hello'

# при присвоении нового значения по несуществуюшему ключу 
# создается новая пара
# аналог метода append. 
my_dict['A'] = 777
print(my_dict)

# удаление элемента 
del my_dict['A']
print(my_dict)

# обновление данных 
data = {'name': 'Vladislav', 'age': 24, "ID": 123.5}
data.update({"age": 35, "ID":300 })
data.update({'Driving licence': "yes"})
print(data)

# my_set = {1,2,3,4,5,6}
# print(my_set)
# print(type(my_set))


# my_tuple = (10,20,30,40,50)
# print(my_tuple)
# print(type(my_tuple))
# print(my_tuple.index(10))
# # чтение значения элементов tuple 
# print(my_tuple[0])
# # срез tuple
# print(my_tuple[2:])


# my_string ="a, b, c, d, e"
# print(my_string)
# print(type(my_string))


