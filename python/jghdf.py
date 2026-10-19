# print("привет")
# print("2+3")

# print("привет")
#    #print("2+3")//неправильео   

# if 1<2: 
#     print("hello")

# print("4+5")
#  #Print(3+4)


# #строчные коментарии 
# #функция выводит информацию на консоль 
# # print("hello world")

# '''блочные коментарии'''
# """блочные коментарии"""

# # #функция выводит информацию на консоль 
# # print("привет" , "как дел")

# name =input("введите имя ")
# print(name)



# '''
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield'''

# # = присваивание 
# name ="fil"
# print("name")

# # camel case
# username = "rue"

# # underscore notation 

# user_name= " rue" 
# # регистрозависимость
# # две разные переменные 
# age=45
# Age=45
# print(age)
# age=34
# print(age)

# # числовые типы данных
# '''
# int- целые числа
# float-вещественные типы ( число с плавающей точкой) x=7,8
# '''

# # текстовой типы данных
# '''
# str- строка это неизм тип данных ( последовательность символов , заключенная в одинарные или двойные кавычки )
# name="h"
# name='e'
# '''


# # логические типы данных
# '''
# bool- логические занчения ( True - истина ,false-лож)
# is_ativate=true'''



# # none
# '''
# NoneType- отсутствие данных 
# is_ativate=nome'''

# x=10
# y=19.7
# desc="описание " 
# is_name=False
# r=None
# print(x,y,desc,is_name,r)

# # 2-10
# A=0b11
# b=0b1011



# # print(a)
# # print(b)
# # print(0b1001)

# # 8-10
# print(0o11)
# print(0o1011)

# # 16-10
# print(0x0A)

# #явное преобразование 
# x=10
# y=str(x) #из числа в строку
# z=float(x) # из строки в вещ тип
# c=bool(x) # из числа в bool
# print(y)
# print(z)
# print(c)

# # x=10
# # t=6
# # d1 = i+t
# # print(d) #int
# # print(type(d))

# # o=10
# # i=6.6
# # d1=i+t
# # print(d1) #float
# # print(type(d1))






# name=input("введите имя ")
# print("привет", name,"!")


# # b= int(input("введите второе число через запятую "))
# # a= int(input("введите первое число через запятую "))
# # print(a+b)


# a= int(input("введите  число через запятую "))
# b= int(input("введите  число через запятую "))
# x=a+b
# print(x)
# print(a+b)

# city= int(input("город  "))
# age= int(input("возраст"))
# print("ты живешь в ", city," и тебе", age,"лет")




# a= int(input("введите  число через запятую "))
# b= int(input("введите  число через запятую "))
# print(b,a)




# v= float(input("введите  длинну "))
# m= float(input("введите  ширину"))
# print("периметр прямоугольника: ' 2*v+2*m ")
# print("ширина прямоугольника'  ")





# a= int(input("введите год рождения "))
# b= int(input("введите текущий год  "))
# print ('ваш возраст', b-a )







# a= (input("введите первое число  "))
# b= (input("введите второе число  "))
# print(type(a))
# print(type(b))
# x=int(a)
# z=int(b)
# print(x+z)





print("КАЛЬКУЛЯТОР")
print("Арифметические операции: ")
print("+  -  *  /  //  %  **")
print("Операции сравнения (True/False): ")
print("==  !=  >  <  >=  <=")

try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    oper = input("Введите операцию: ")

    result = None

    if oper == "+":
        result = a + b
        print("Сумма: ",result)

    elif oper == "-":
        result = a - b
        print("Разность: ",result)

    elif oper == "*":
        result = a * b
        print("Произведение: ",result)

    elif oper == "/":
        if b == 0:
            print("Ошибка: на ноль делить нельзя")
        else:
            result = a / b
            print("Частное: ",result)

    elif oper == "//":
        if b == 0:
            print("Ошибка: на ноль делить нельзя")
        else:
            result = a // b
            print("Целое частное: ",result)

    elif oper == "%":
        if b == 0:
            print("Ошибка: на ноль делить нельзя")
        else:
            result = a % b
            print("Остаток: ",result)

    elif oper == "**":
        result = a ** b
        print(f"Число {a} в степени {b}: ",result)

    elif oper == "==":
        result = a == b
        print("Истинность: ",result)

    elif oper == "!=":
        result = a != b
        print("Истинность: ",result)

    elif oper == ">":
        result = a > b
        print("Истинность: ",result)

    elif oper == "<":
        result = a < b
        print("Истинность: ",result)

    elif oper == ">=":
        result = a >= b
        print("Истинность: ",result)

    elif oper == "<=":
        result = a <= b
        print("Истинность: ",result)

    else:
        print("Ошибка! Такой операции нет.")

    print("\nЛогические операторы:")

    if a > 0 and b > 0:
        print("Оба числа положительные")

    if a > 0 or b > 0:
        print("Хотя бы одно число положительное")

    if not a == b:
        print("Числа не равны")

    # операторы принадлежности (in, not in)
    operations = ["+", "-", "*", "/", "//", "%", "**"]

    if oper in operations:
        print("Операция - арифметическая")

    if oper not in operations:
        print("Операция сравнения")

    # операторы тождественности (is, is not)
    if result is None:
        print("Результат отсутствует")

    if result is not None:
        print("Результат существует")

except ValueError:
    print("Ошибка: нужно вводить числа")

























