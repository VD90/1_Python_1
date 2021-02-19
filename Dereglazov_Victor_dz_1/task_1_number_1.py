# untill seconds
duration = int(53)
s = duration % 60
print("duration =", duration, "секунд")
print(s, "сек")

# untill minutes
duration = int(153)
m = duration // 60
s = duration % 60
print("duration =", duration, "секунд")
print(m, "мин", s, "сек")

# untill hours
duration = int(4153)
h = duration // 60 // 60
m = duration // 60 % 60
s = duration % 60
print("duration =", duration, "секунд")
print(h, "час", m, "мин", s, "сек")

# *untill 24 hours
duration = int(5000000)
d = duration // 60 // 60 // 24
h = duration // 60 // 60 % 24
m = duration // 60 % 60
s = duration % 60
print("duration =", duration, "секунд")
print(d, "день", h, "час", m, "мин", s, "сек")