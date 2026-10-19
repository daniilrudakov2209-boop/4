print('МНОЖЕСТВА')

nums = [1, 2, 3, 2, 1, 4, 5, 4, 3]
s1 = set(nums)
print("Множества задача 1:", s1, "| Количество:", len(s1))


s2 = {10, 20, 30}
s2.add(40)
s2.remove(20)
print("Множества задача 2:", s2)

a = {1, 2, 3}
b = {3, 4, 5}


print("Множества задача 3:", a.union(b))


print("Множества задача 4:", a.intersection(b))


print("Множества задача 5:", a.difference(b), "|", b.difference(a))


print("Множества задача 6:", a.symmetric_difference(b))


x = 2
print("Множества задача 7:", x in a)


c = {1, 2}
d = {1, 2, 3, 4}
print("Множества задача 8:", c.issubset(d))


text = "hello world"
chars = set(text)
print("Множества задача 9:", chars, "| Количество:", len(chars))


list1 = [1, 2, 2, 3, 4, 5]
list2 = [4, 5, 5, 6, 7, 2]
common = sorted(set(list1) & set(list2))
print("Множества задача 10:", common)

print('')
print('КОРТЕЖИ')

print("Кортежи задача 1. Первый, последний и средний элементы:")
numbers = (10, 20, 30, 40, 50)
print("Кортежи задача 1.", numbers[0], numbers[-1], numbers[len(numbers) // 2])

print("Кортежи задача 2. Первые два, последние два и обратный порядок")
numbers = (1, 2, 3, 4, 5, 6, 7, 8)
print("Кортежи задача 2. Первые два числа:", numbers[:2])
print("Последние два числа:", numbers[-2:])
print("Обратный порядок:", numbers[::-1])

print ("Кортежи задача 3. Длина, сумма, минимум и максимум:")
numbers = (12, 5, 8, 20, 3, 15)
print("Кортежи задача 3. Длина:", len(numbers))
print("Сумма:", sum(numbers))
print("Минимум:", min(numbers))
print("Максимум:", max(numbers))

print("Кортежи задача 4. Проверка числа, количество и индекс:")
numbers = (2, 5, 3, 5, 7, 5, 9)
x = 5
print("Кортежи задача 4. Есть ли число:", x in numbers)
print("Количество:", numbers.count(x))
print("Индекс:", numbers.index(x))

print("Кортежи задача 5. Объединение двух кортежей:")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Кортежи задача 5.", tuple1 + tuple2)

print("Кортежи задача 6. Кортеж из одного элемента:")
my_tuple = (10,)
print("Кортежи задача 6.", my_tuple)
print("Тип:", type(my_tuple))

print("Кортежи задача 7. Распаковка кортежа:")
person = ("Иван", 18, "Москва")
name, age, city = person
print("Имя:", name)
print("Возраст:", age)
print("Город:", city)

print("Кортежи задача 8. Обмен значениями переменных:")
a = 10
b = 20
a, b = b, a
print("Кортежи задача 8. a =", a, "b =", b)

print("Кортежи задача 9. Замена второго элемента:")
numbers = (10, 20, 30, 40)
new_numbers = numbers[:1] + (99,) + numbers[2:]
print("Кортежи задача 9.", new_numbers)

print("Кортежи задача 10. Удаление повторов и сортировка:")
numbers = (5, 2, 8, 2, 1, 5, 3, 8, 1)
result = tuple(sorted(set(numbers)))
print("Кортежи задача 10.", result)