user_input = input("Enter words separated by whitespace: ")

list_a = user_input.split(' ')

list_b = sorted(list(set(list_a)))

print(*list_b)
