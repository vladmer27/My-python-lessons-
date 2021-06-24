# *** Генератор паролей*** 

# через import скачиваются библиотеки
import hashlib 
from tkinter import Tk, Label, Entry, Button, StringVar

def hashing():
    # """""" для многострочных объектов и документации
    """ 
    функция хэширования
    
    принимает строку пароль и "соль"
    возвращает хеш-строку
    """

    # прием строки человекочитаемой пароли с "солью"
    pwd_str = pwd.get()
    # кодирование в байт-строку 
    byte_str = pwd_str.encode()
    # хэширование  (применение хэш-функций из модуля hashlib) 
    hash_str = hashlib.sha256(byte_str)
    # преобразование хэш-строки специального типа в обычную строку типа str
    hex_str = hash_str.hexdigest()[:10]
    # передача зашехированной строки
    hash_pwd.set(hex_str)


    # print(hex_str)
    # print(type(hex_str))
# hashing("qwerty")

# объект окна 
window = Tk()
window.title("Password generator v.0.1")

# переменные класса stringVar 
pwd = StringVar()
hash_pwd = StringVar()

# виджет (компонент) текстовой метки 
Label(text='пароль:').grid(row=0, column =0, padx = 5, pady = 5)

# виджет поля ввода 
Entry(textvariable=pwd).grid(row=0, column =1, padx = 5, pady = 5)

# виджет кнопки 
Button(text= 'Start', command=hashing).grid(row=2, column =0, padx = 5, pady = 5)

# виджет поля вывода
Entry(textvariable=hash_pwd).grid(row=1, column =1, padx = 5, pady = 5)

# запуск программы (точка входа программы) 
window.mainloop()
