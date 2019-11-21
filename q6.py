import math
user_input = input("Enter Input separated by comma:")

list_a = user_input.split(',')
list_b = []
for i in list_a:
    list_b.append(int(math.sqrt((2*50*int(i))/30)))

print(*list_b, sep = ',')


