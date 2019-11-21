user_input = input("Enter 2 digits separated by comma:")
list_a = (user_input.split(','))

x = int (list_a[0])  
y = int (list_a[1]) 
list_a = []
list_b = []


for i in range(0,x):
    print(i)
    for j in range(0,y):
        list_b.append(i*j)

    print(list_b)
    list_a.append(list_b)
    list_b = []

print(list_a)
