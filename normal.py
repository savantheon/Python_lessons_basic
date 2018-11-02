# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
from easy import md
from easy import dir
from easy import rd
from easy import cd
import os
import sys
print("Поздорову, барин! Чего желаете?")
print("1)Создать папку")
print("2)Посмотреть содержимое текущей папки")
print("3)Удалить папку")
print("4)Перейти в папку")

x=input()
if(x=="1"):
    print("Барин, укажите имя папки")
    dir_name=str(input())
    if os.path.exists(dir_name):
        print("Ошибочка, барин, есть такая папка!")
    else:
        md(dir_name)
        print("Папка успешно создана")
elif(x=="2"):
    dir()
elif(x=="3"):
    print("Барин, укажите имя папки")
    dir_name=str(input())
    if os.path.exists(dir_name):
        rd(dir_name)
        print("Папка успешно удалена")
    else:
        print("Ошибочка, барин, нема такой папки")
elif(x=="4"):
    print("Барин, укажите имя папки")
    dir_name=str(input())
    cd(dir_name)
    print(os.getcwd())
    print("Faster, then light jump succesefull!")

    print(os.getcwd())
else:
    print("Извольте выразиться яснее, барин")

