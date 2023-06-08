import sys

def find_pairs(numbers):
    """
    Функція приймає список чисел та повертає список пар чисел, сума яких рівна 10.
    """
    pairs = []
    for i, x in enumerate(numbers):
        for y in numbers[i+1:]:
            if x + y == 10:
                pairs.append((x, y))
    return pairs

if __name__ == '__main__':
    # Отримання списку чисел з аргументів командного рядка
    numbers = [int(x) for x in sys.argv[1:]]

    # Знаходження пар чисел, сума яких рівна 10
    pairs = find_pairs(numbers)

    # Виведення знайдених пар на екран
    for pair in pairs:
        print(f'{pair[0]} + {pair[1]}')
