user_input = input("Type words separated by comma:")

list_a = user_input.split(',')

list_b = sorted(list_a)

print(*list_b,sep = ',')
