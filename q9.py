lines = []

while True:
    l = input()
    if l:
        lines.append(l.upper())
    else:
        break;

for i in lines:
    print(i)
