
print("Задание 1")
list1 = [10, 20, 30, 40, 50]
print("Первый элемент:", list1[0])
print("Последний элемент:", list1[-1])
list1[0], list1[-1] = list1[-1], list1[0]
print("После обмена:", list1)



print("Задание 2")
list2 = [1, 2, 3, 4, 5]
mid = len(list2) // 2
print("Средний элемент:", list2[mid])



print("Задание 3")
list3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Первые три:", list3[:3])
print("Последние три:", list3[-3:])
print("С чётными индексами:", list3[::2])
print("В обратном порядке:", list3[::-1])



print("Задание 4")
list4 = []
list4.append(10)
list4.append(20)
list4.append(30)
list4.insert(0, 5)
list4.pop()
print("Результат:", list4)


print("Задание 5")
list5 = [4, 8, 15, 16, 23, 42]
print("Длина:", len(list5))
print("Сумма:", sum(list5))
print("Минимум:", min(list5))
print("Максимум:", max(list5))
print("Среднее арифметическое:", sum(list5) / len(list5))



print("Задание 6")
list6 = [5, 2, 9, 2, 7, 2, 3]
x = 2
print("Есть ли x в списке:", x in list6)
print("Количество вхождений:", list6.count(x))
print("Индекс первого вхождения:", list6.index(x))



print("Задание 7")
list7 = [45, 12, 78, 3, 56, 89, 1]
s_list7 = sorted(list7)
print("Три наименьших:", s_list7[:3])
print("Три наибольших:", s_list7[-3:])


print("Задание 8 ")
list1 = [5, 2, 9]
list2 = [8, 1, 6]
combined = sorted(list1 + list2, reverse=True)
print("Объединенный по убыванию:", combined)
print("Второй по величине:", combined[1])



print("Задание 9")
s9 = "вишня яблоко банан апельсин"
words = s9.split()
words.sort()
result_s9 = ", ".join(words)
print("Результат:", result_s9)



print("Задание 10")
lst10 = [1, 2, 3, 4, 5]
k = 2
res10 = lst10[-k:] + lst10[:-k]
print("Сдвиг вправо на", k, ":", res10)