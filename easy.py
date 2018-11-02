# Автор: Соколов Андрей Николаевич
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
import sys
def md(directory_name):
    k=os.mkdir(directory_name)
    return k
def dir():
    z=[]
    k=os.listdir(os.getcwd())
    print(k)
    '''for i in range(0,len(k)):
        if(os.path.isdir(k[i])==True):
                   z.append(k[i])
                   return z'''
def md(directory_name):
    os.mkdir(directory_name)
def rd(directory_name):
    os.rmdir(directory_name)
def cd(directory_name):
    os.chdir(directory_name)
def dir1_9c(directory_name):
    os.mkdir("dir_1")
    os.mkdir("dir_2")
    os.mkdir("dir_3")
    os.mkdir("dir_4")
    os.mkdir("dir_5")
    os.mkdir("dir_6")
    os.mkdir("dir_7")
    os.mkdir("dir_8")
    os.mkdir("dir_9")
def dir1_9d(directory_name):
    os.rmdir("dir_1")
    os.rmdir("dir_2")
    os.rmdir("dir_3")
    os.rmdir("dir_4")
    os.rmdir("dir_5")
    os.rmdir("dir_6")
    os.rmdir("dir_7")
    os.rmdir("dir_8")
    os.rmdir("dir_9")
def copy(target_name):
    k=os.path.basename(sys.argv[0]).split(".")
    z=k[0]+'_copy.'+k[1]
    shutil.copy(os.path.basename(sys.argv[0]), z)
    print ("Копия успешно создана")
"""print("Выберите задание")
print("1а. Создать папки")
print("1б. Удалить папки")
print("2. Узнать папки текущей директории")
print("3. Создать копию файла")
a=input()
if(a=="1а"):
    os.mkdir("dir_1")
    os.mkdir("dir_2")
    os.mkdir("dir_3")
    os.mkdir("dir_4")
    os.mkdir("dir_5")
    os.mkdir("dir_6")
    os.mkdir("dir_7")
    os.mkdir("dir_8")
    os.mkdir("dir_9")
    print("Выполнено! Папки созданы")
elif(a=="1б"):
    os.rmdir("dir_1")
    os.rmdir("dir_2")
    os.rmdir("dir_3")
    os.rmdir("dir_4")
    os.rmdir("dir_5")
    os.rmdir("dir_6")
    os.rmdir("dir_7")
    os.rmdir("dir_8")
    os.rmdir("dir_9")
    print("Выполнено! Папки удалены")
elif(a=="2"):
    print("Вижу следующие папки:")
    k=os.listdir(os.getcwd())
    for i in range(0,len(k)):
        if(os.path.isdir(k[i])==True):
                   print(k[i])
elif(a=="3"):
    k=os.path.basename(sys.argv[0]).split(".")
    z=k[0]+'_copy.'+k[1]
    shutil.copy(os.path.basename(sys.argv[0]), z)
    print ("Копия успешно создана")
else:
    print("Такого задания нет")"""

