import random

numbers = []
for i in range(100):
    numbers.append(random.randint(0, 100))
print(numbers)


avto_models = ['BMW', 'Mercedes', 'Lada', 'УАЗ']
models: "Под санкциями" = 'BMW', 'Mercedes'
models: "Не под санкциями" = 'Lada','УАЗ'

print('Она под санкциями')

