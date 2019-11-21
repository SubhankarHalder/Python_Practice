import random
sample_number = random.randint(5,11)
print(f"Sample Number: {sample_number}")

list_a = list(range(1, sample_number+1))

dict_a = {i: i*i for i in list_a}

print(f"Dictionary: {dict_a}")
