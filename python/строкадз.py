print("1. Длина, первый и последний символы")
s = "программирование"
print("Строка:", s)
print("Длина:", len(s))
print("Первый символ:", s[0])
print("Последний символ:", s[-1])

print("2. Середина строки")
mid = len(s) // 2
if len(s) % 2 == 0:
  print("Средние символы:", s[mid - 1 : mid + 1])
else:
  print("Средний символ:", s[mid])

print("3. задание ")
print("Первые три:", s[:3])
print("Последние три:", s[-3:])
print("С чётными индексами:", s[::2])
print("В обратном порядке:", s[::-1])

print("4. задание")
text = "привет мир"
print("Верхний:", text.upper())
print("Нижний:", text.lower())
print("С заглавной:", text.capitalize())

print("5.задание")
c = "р"
print(f"Символ '{c}' есть в строке:", c in s)
print(f"Количество вхождений '{c}':", s.count(c))
print(f"Индекс первого вхождения '{c}':", s.find(c))

print("6.задание")
phrase = "это строка с пробелами"
print("Результат:", phrase.replace(" ", "_"))

print("7.задание")
messy_str = "   текст с пробелами   "
clean_str = messy_str.strip()
print("Длина без пробелов:", len(clean_str))

print("8. задание")
full_name = "Иван Иванов"
parts = full_name.split()
name, surname = parts[0], parts[1]
print("Фамилия и имя:", surname, name)
print("Инициалы:", f"{surname} {name[0]}.")

print("9.задание")
palindrome = "А роза упала на лапу Азора"
s_clean = palindrome.replace(" ", "").lower()
print("Это палиндром:", s_clean == s_clean[::-1])

print("10.задание")
sentence = "я изучаю язык программирования пайтон"
words = sentence.split()
print("Количество слов:", len(words))
print("Первое слово:", words[0])
print("Последнее слово:", words[-1])