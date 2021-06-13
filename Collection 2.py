# tuple
# a = (1,2,3,4,5,6)
# print(a)
# print(type(a))
# print(len(a))
# print(2 in a)


# # list
# b = [1,2,3,4,5,6]
# print(b)
# print(type(b))
# print(len(b))
# print(2 in b) 
# print(b.count(2))


# set
# c = {1,2,3,4,5,6}
# print(c)
# c.add(123)

# print(type(c))
# print(len(c))
# print(2 in c)
c = {10,20,30}
# добавление множества
c.add(30)
print(c)
c.remove(20)
# c.remove(123)
# print(c)

# метод удаления без ошибок 
c.discard(10)

# Дано два множества 
W = {"A", 'B', 'C', 'D', 'E'}
Z = {'B', 'C', 'Q'}

# объединить 
# F = W.union(Z)
F = W | Z
# print(F)

# КАК КРУГИ ЭЙЛЕРА
# пересечение 
F = W.intersection(Z)
# короткая запись пересечение 
F = W&Z
print(F)

# разность 
F = W.difference(Z)
F = Z.difference(W)
F = W.symmetric_difference(Z)
# короткая запись symmetric difference 
F = W - Z
# СРС эксперименты с оставшимися методами 
# print(F)


# # dict
# d = {'a': 1, 'b': 2, "c":3, 'd':4, 'e':5}
# print(d)
# print(type(d))
# print(len(d))
# print('a' in d)
# print('a' in d.keys())
# print(2 in d.values())
# print(('a', 1) in d.items())


# # string 
# e = "hello 1 world"
# print(e)
# # print(len(e))
# # print('e' in e)
# # print("hello" in "hellow world")
# # print(e.count('h'))
# # print(e.index('h'))
# print(e[-1])
# e1= e[2:]
# print(e1)



