list_a = list(range(2000,3200))
list_b = []
for i in list_a:
    if (i%7 == 0) and (i%5 != 0):
        list_b.append(i)
print(*list_b, sep = ',')

