import random

def rand_string():
    list_a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    string_a = random.choices(list_a,k=29)
    return string_a

def rand_char():
    list_a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    return random.choice(list_a)

def check(x, truth, counter):
    if x == "me thinks it is like a weasel":
        truth += 1
        counter += 1
    else:
        counter += 1

    return truth, counter

def main():
    string_b = rand_string()
    truth = 0
    counter = 0
    truth, counter = check(string_b, truth, counter)

    while (counter < 1000) and (truth == 0):
        if string_b[0] != 'm':
            list_b = list(string_b)
            list_b[0] = rand_char()
            string_b = ''.join(list_b)
        else string_b[1] != 'e':
            list_b = list(string_b)
            list_b[1] = rand_char()
            string_b = ''.join(list_b)
        else string_b[2] != ' ':
            list_b = list(string_b)
            list_b[2] = rand_char()
            string_b = ''.join(list_b)
        else string_b[3] != 't':
            list_b = list(string_b)
            list_b[3] = rand_char()
            string_b = ''.join(list_b)
        else string_b[4] != 'h':
            list_b = list(string_b)
            list_b[4] = rand_char()
            string_b = ''.join(list_b)
        else string_b[5] != 'i':
            list_b = list(string_b)
            list_b[5] = rand_char()
            string_b = ''.join(list_b)
        else string_b[6] != 'n':
            list_b = list(string_b)
            list_b[6] = rand_char()
            string_b = ''.join(list_b)
        else string_b[7] != 'k':
            list_b = list(string_b)
            list_b[7] = rand_char()
            string_b = ''.join(list_b)
        else string_b[8] != 's':
            list_b = list(string_b)
            list_b[8] = rand_char()
            string_b = ''.join(list_b)
        else string_b[9] != ' ':
            list_b = list(string_b)
            list_b[9] = rand_char()
            string_b = ''.join(list_b)
        else string_b[10] != 'i':
            list_b = list(string_b)
            list_b[10] = rand_char()
            string_b = ''.join(list_b)
        else string_b[11] != 't':
            list_b = list(string_b)
            list_b[11] = rand_char()
            string_b = ''.join(list_b)
        else string_b[12] != ' ':
            list_b = list(string_b)
            list_b[12] = rand_char()
            string_b = ''.join(list_b)
        else string_b[13] != 'i':
            list_b = list(string_b)
            list_b[13] = rand_char()
            string_b = ''.join(list_b)
        else string_b[14] != 's':
            list_b = list(string_b)
            list_b[14] = rand_char()
            string_b = ''.join(list_b)
        else string_b[15] != ' ':
            list_b = list(string_b)
            list_b[15] = rand_char()
            string_b = ''.join(list_b)
        else string_b[16] != 'l':
            list_b = list(string_b)
            list_b[16] = rand_char()
            string_b = ''.join(list_b)
        else string_b[17] != 'i':
            list_b = list(string_b)
            list_b[17] = rand_char()
            string_b = ''.join(list_b)
        else string_b[18] != 'k':
            list_b = list(string_b)
            list_b[18] = rand_char()
            string_b = ''.join(list_b)
        else string_b[19] != 'e':
            list_b = list(string_b)
            list_b[19] = rand_char()
            string_b = ''.join(list_b)
        else string_b[20] != ' ':
            list_b = list(string_b)
            list_b[20] = rand_char()
            string_b = ''.join(list_b)
        else string_b[21] != 'a':
            list_b = list(string_b)
            list_b[21] = rand_char()
            string_b = ''.join(list_b)
        else string_b[22] != ' ':
            list_b = list(string_b)
            list_b[22] = rand_char()
            string_b = ''.join(list_b)
        else string_b[23] != 'w':
            list_b = list(string_b)
            list_b[23] = rand_char()
            string_b = ''.join(list_b)
        else string_b[24] != 'e':
            list_b = list(string_b)
            list_b[24] = rand_char()
            string_b = ''.join(list_b)
        else string_b[25] != 'a':
            list_b = list(string_b)
            list_b[25] = rand_char()
            string_b = ''.join(list_b)
        else string_b[26] != 's':
            list_b = list(string_b)
            list_b[26] = rand_char()
            string_b = ''.join(list_b)
        else string_b[27] != 'e':
            list_b = list(string_b)
            list_b[27] = rand_char()
            string_b = ''.join(list_b)
        else string_b[28] != 'l':
            list_b = list(string_b)
            list_b[28] = rand_char()
            string_b = ''.join(list_b)

        truth, counter = check(string_b, truth, counter)

if __name__ = __main__:
    main()
