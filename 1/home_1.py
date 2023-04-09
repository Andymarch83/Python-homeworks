# Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = str(input("Введите трёхзначное число: "))
total = int(number[0]) + int(number[1]) + int(number[2])
print(number, "->", total, " ",  "(", number[0],
      "+", number[1], "+", number[2], ")")

