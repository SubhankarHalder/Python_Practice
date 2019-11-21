import random

sample_number = random.randint(1, 10)

def factorial(n):
    if (n==1):
        return 1
    else:
        return(n*factorial(n-1))
        

print(f"Sample Number is {sample_number}")
print(f"Factorial is {factorial(sample_number)}")

