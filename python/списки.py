# # Списки в Python - это изменяемые последовательности элементов,
# # которые могут содержать данные любого типа: числа, строки,
# # другие списки и даже объекты. Списки позволяют хранить упорядоченные
# # коллекции элементов, доступ к которым можно получить по индексу.


# my_list = []
# print(my_list)

# my_list = [ 1,2,3,True, "dglfsgklsfg",None]
# print(my_list)

# my_list.append("new_element")  # Добавление элемента в конец списка
# print(my_list)

# my_list.insert(2, "два")  # Вставка элемента по индексу
# print(my_list)

# my_list.extend([4, 5, 6])  # Расширение списка другим списком
# print(my_list)

# my_list.remove(2)  # Удаление элемента по значению
# print(my_list)

# last_element = my_list.pop()  # Удаление последнего элемента и его возврат
# print(last_element)
# print(my_list)

# my_list.pop(-1)
# print(my_list)  

# my_list.clear()  # Очистка списка
# print(my_list)



# list2 = [1, 2, 3, 4, 5,3,3]
# index = list2.index(3)  # Получение индекса элемента по значению
# print(index)



# count = list2.count(3)  # Подсчет количества вхождений элемента
# print(count)


# list1 = [5, 2, 9, 1, 5, 6]
# list1.sort()  # Сортировка списка
# list1.sort(reverse=True)  # Сортировка списка в обратном порядке
# print(list1)

# list4 = [1, 2, 3, 4, 5]
# list4.reverse()  # Разворот списка
# print(list4)

# list5 = [ 23,4,5,56,4,42]
# sorted= sorted(list5)  # Возвращает новый отсортированный список
# print(sorted)
# print (list5)    


# print(len(sorted))  # Длина списка

# print(min(sorted))  # Минимальный элемент списка
# print(max(sorted))  # Максимальный элемент списка
# print(sum(sorted))  # Сумма элементов списка

# list6 = [1, 2, 3, 4, 5]
# print(list6[0])  # Доступ к элементу по индексу
# print(list6[-1])  # Доступ к последнему элементу списка
# print(list6.copy())  # Создание копии списка
# print(list6[:])  # Создание среза списка
# print(list6[::])  
# print(list6[::2]) # Срез с шагом
# print(list6[1::2])  # Срез с шагом, начиная со второго элемента
# print(list6[::-1])  # Разворот списка с помощью среза
# print(list6[:4]) 
# print(list6[2:])  # Срез с указанием начала
# print(list6[-2:1:-1])    


# list6[0] = 1000
# print(list6)  # Изменение элемента списка по индексу

# matrix = [[1, 2, 3], [4, 5, 6],]
# print(matrix[1][2])  # Доступ к элементу вложенного списка


# list9=list(range(11))  # Создание списка с помощью функции range
# print(list9)

# a=[x**2 for x in range(5)]
# print(a)

# s=[1,2,3]
# s1 = [12,13,14]
# print(s1+s)  # Конкатенация списков

# s= [1,2,3,4]
# a,b,c,f=s  # Распаковка списка в переменные
# print(a,b,c,f)

# a,_,b,f=s  # Распаковка списка с использованием переменной _ для игнорирования значения
# print(a,b,f)

# a,*b,c=s  # Распаковка списка с использованием * для сбора оставшихся элементов в список
# print(a,b)


# listFRUKT = ["яблоко", "банан", "вишня", "апельсин", "груша"]
# print(listFRUKT)      
# print(listFRUKT[0])   
# print(listFRUKT[-1])  
# print(listFRUKT[2])   



import random

Random = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
secret = random.choice(Random)

print('Загадано одно число из 10. Угадайте его.')
print()

guess = int(input("Попытка 1/3: "))
if guess != secret:
    if guess in Random:
        Random.remove(guess)
    else:
        print("Этого числа  нет в списке!")
    
    guess = int(input('Не угадали. Попытка 2/3: '))
    if guess != secret:
        if guess in Random:
            Random.remove(guess)
        else:
            print("Этого числа  нет в списке!")
        
        guess = int(input('Не угадали. Попытка 3/3: '))
        if guess != secret:
            if guess in Random:
                Random.remove(guess)
            else:
                print("Этого числа  нет в списке!")
            print('Не угадали. Загаданное число:', secret)
        else:
            print("Угадали!")
    else:
        print("Угадали!")
else:
    print("Угадали!")