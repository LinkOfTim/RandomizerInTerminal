from random import randint, sample
import statistics

# Цветной вывод
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'

def input_int(prompt: str) -> int:
    try:
        return int(input(prompt))
    except ValueError as e:
        print(f'{Color.RED}Input error: {e}{Color.RESET}')
        exit(1)

# Ввод данных
count_number = input_int('Enter count of random numbers: ')
left_border = input_int('Enter left border: ')
right_border = input_int('Enter right border: ')

if left_border >= right_border:
    print(f'{Color.RED}Error: Left border must be less than right border{Color.RESET}')
    exit(1)

# Выбор уникальности
unique_choice = input('Unique numbers only? (y/n): ').strip().lower()
use_unique = unique_choice == 'y'

if use_unique and count_number > (right_border - left_border + 1):
    print(f'{Color.YELLOW}Warning: Too many numbers for unique selection, some numbers will repeat{Color.RESET}')
    use_unique = False

# Генерация чисел
if use_unique:
    numbers = sample(range(left_border, right_border + 1), count_number)
else:
    numbers = [randint(left_border, right_border) for _ in range(count_number)]

# Сортировка
sort_choice = input('Sort numbers? (y/n): ').strip().lower()
if sort_choice == 'y':
    numbers.sort()

# Вывод чисел с цветом
colored_numbers = [f"{Color.BLUE}{num}{Color.RESET}" for num in numbers]
print("Generated numbers:", " ".join(colored_numbers))

# Статистика
print(f"{Color.GREEN}Min: {min(numbers)}, Max: {max(numbers)}, Average: {round(statistics.mean(numbers), 2)}{Color.RESET}")

