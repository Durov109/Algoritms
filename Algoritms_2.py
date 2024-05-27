''' Две числовые переменные надо поменять друг с другом '''

a = 4
b = 5
c = a
a = b
b = c
print(f"input a=4 b=5")
print(f"output a={a}, b={b}")

a = 4
b = 5
a = a + b
b = a - b
a = a - b

print(f"input a=4 b=5")
print(f"output a={a}, b={b}")

#############################################################################

''' Найти максимальное значение переменной из 3-х существующих '''

num = [-89, -2, -3]
max_num = num[0]

for i in num:
    if i > max_num:
        max_num = i
print(max_num)



num = [-89, -2, -3, -40]
max_num = float("-inf")

for i in num:
    if i > max_num:
        max_num = i
print(max_num)

#############################################################################

''' Определение ФИО из строки с неопределенных кол-м пробелов '''

a = "Ivanov                   Ivan     Ivanovich"
sur_name_patronymic = ""
word = ""

for i in a:
    if i != " ":
        word += i
    else:
        if word:
            sur_name_patronymic += word + " "
            word = ""

sur_name_patronymic += word

print(sur_name_patronymic)


#############################################################################

''' Перевернуть строку '''

a = "hello world"
lenght = 0

for i in a:
    lenght += 1

for i in range(lenght-1, -1, -1):
    print(a[i], end="")


#############################################################################

''' Найти среднее афирм. и заменить минимальный элемент на сред. арифм. '''
numbers = [-1, -2, -3, -5, -10]
count = 0
summa = 0

for i in numbers:
    count += 1

for i in numbers:
    summa += i

average = summa / count
min_num = numbers[0]
index = 0

for i in numbers:
    if i < min_num:
        min_num = i
        index += 1

numbers[index] = average

print(numbers)


#############################################################################

''' Убрать условный опратор, если а=0 тогда b=2, иначе b=1'''
A = 0
B = 2 - A
print(B)  # Выведет 2

A = 1
B = 2 - A
print(B)  # Выведет 1

#############################################################################

''' Отсортировать два массива по возрастанию '''

list_1 = [1, 3, 4, 7, 8]
list_2 = [-1, 0, 2, 5, 6, 9]
join_list = list_1 + list_2

lenght = 0
for i in join_list:
    lenght += 1


for num in range(1, lenght):
    index = num
    while index > 0 and join_list[index-1] > join_list[index]:
        join_list[index], join_list[index-1] = join_list[index-1], join_list[index]
        index -= 1

print(join_list)

