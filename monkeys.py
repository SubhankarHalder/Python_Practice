import random

def rand_funct():
    list_a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z',' ']
    
    list_b = random.choices(list_a, k=28)
    
    string_a = ''.join(list_b)
    return string_a

def score_func(x,truth, counter):

    if x == "methinks it is like a weasel":
        truth += 1
        counter += 1
    else:
        counter += 1

    return truth,counter

def main():
    string_b = rand_funct()
    truth = 0
    counter = 0
    truth, counter = score_func(string_b,truth, counter)
    while counter < 1000 and truth == 0:
        string_b = rand_funct()
        truth,counter = score_func(string_b, truth, counter)

    print(string_b)
    print(counter)
    print(truth)

if __name__ == "__main__":
    main()

