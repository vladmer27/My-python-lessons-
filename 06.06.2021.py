# # dict 
# a = {}
# print (type(a))

# # set
# b = {1,2,3}
# print(type(b))

# # dict 
# c = {'a':1, 'b': 2, 'c':3}
# print (type(c))
# print(c)

# my_list = ['a', 'b', 'c', 'd', 'e', 'f']
# # Проверка принадлежности элемента с помощью оператора in
# print('a' in my_list)
# print('q' not in my_list)
# print('g' not in my_list)
# print('e' in my_list)

# my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
# # Проверка принадлежности элемента с помощью оператора in
# print('a' in my_dict)
# print('a' in my_dict.keys())
# print('a' in my_dict.values())
# print(1 in my_dict.values())
# # проверка пар 
# print(('a',1) in my_dict.items())
# print(('a',2) in my_dict.items())
# # поиск подстроки 
# print('ab' in 'abc')

# # функция len() - подсчет символов в коллекции 
# print(len(my_list))
# print(len(my_dict))
# print(len('abc'))

# for elm in my_list:
#     print(elm)
# for elm in my_dict:
#     print(elm)
# for elm in my_dict.values():
#     print(elm) 
# for key, value in my_dict.items():
#     # проход по .items() возвращает кортеж (ключ, значение),
#     # который присваивается кортежу переменных key, value
#     print(key, value) 

# # поиск максимального значения, минимального значения, суммы
# print(min(my_list))
# print(sum(my_dict.values()))

 
my_list = [1,2,2,2,2,4]

# .count = подсчет для неуникальных коллекций
print(my_list.count(2))
print(my_list.count(5))

# .copy() метод возвращает неглубокую (нерекурсивную) копию 
# коллекции (list, dict, set) 
my_set = {1, 2, 3}
my_set_2 = my_set.copy()
print(my_set_2 == my_set)
print(my_set_2 is my_set)

# .clear - удаление из коллекций (list, set, dict)
my_set = {1, 2, 3}
print(my_set)
# my_set.clear()
# print(my_set)
my_set.remove(2)
print(my_set)

# .index для list, string, tuple 
my_list_2= [1,2,3,4,5,6,7,5,8] 
print(my_list_2.index(2))
print(my_list_2.index(5))

# ***методы сравнения множеств set_a и set_b

set_a = {1,2,3,4,5,6,}
set_b = {1,2,3,4,5,6,7,8,9,10}
set_c = {2,6,9,10,5,7,9}
set_d = {1,2,3,4,5,6}

# isdisjoint- истина, если set_a и set_b не имеют общих элементов
print(set_a.isdisjoint(set_c))

#issubest - множество входит в другое можество
print(set_a.issubset(set_b))

# issuperset - надмножество 
print(set_b.issuperset(set_a))

print(set_a.issuperset(set_d))
print(set_a.issubset(set_d))

# конвертация одного типа коллекции в другой
my_tuple = ('a', 'b', 'a')
my_list = list(my_tuple)
my_set = set(my_tuple)	
my_frozenset = frozenset(my_tuple)
print(my_list, my_set, my_frozenset)


