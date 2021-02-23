# untill seconds
duration = int(input("Введите время в секундах: "))
s = duration % 60
print("duration =", duration, "секунд")
print(s, "сек")

# untill minutes
duration = int(input("Введите время в секундах: "))
m = duration // 60
s = duration % 60
print("duration =", duration, "секунд")
print(m, "мин", s, "сек")

# untill hours
duration = int(input("Введите время в секундах: "))
h = duration // 60 // 60
m = duration // 60 % 60
s = duration % 60
print("duration =", duration, "секунд")
print(h, "час", m, "мин", s, "сек")

# *untill 24 hours
duration = int(input("Введите время в секундах: "))
d = duration // 60 // 60 // 24
h = duration // 60 // 60 % 24
m = duration // 60 % 60
s = duration % 60
print("duration =", duration, "секунд")
print(d, "день", h, "час", m, "мин", s, "сек")
