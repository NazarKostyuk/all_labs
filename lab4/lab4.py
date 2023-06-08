import os

while True:
    # Запитуємо в користувача шлях до файлу
    file_path = input("Введіть шлях до файлу: ")

    # Перевіряємо чи файл існує
    if not os.path.exists(file_path):
        print("Файл не існує.")
        continue

    # Відкриваємо файл у режимі читання
    with open(file_path, 'r') as file:
        # Ініціалізуємо змінні для зберігання статистики
        line_count = 0
        empty_line_count = 0
        z_line_count = 0
        z_count = 0
        and_line_count = 0

        # Проходимо по кожному рядку у файлі
        for line in file:
            line_count += 1

            # Перевіряємо чи рядок порожній
            if not line.strip():
                empty_line_count += 1

            # Перевіряємо чи рядок містить літеру "z"
            if "z" in line:
                z_line_count += 1

            # Рахуємо кількість літер "z" у файлі
            z_count += line.count("z")

            # Перевіряємо чи рядок містить групу символів "and"
            if "and" in line:
                and_line_count += 1

        # Друкуємо статистику
        print("Статистика для файлу '{}':".format(file_path))
        print("Кількість рядків: {}".format(line_count))
        print("Кількість порожніх рядків: {}".format(empty_line_count))
        print("Кількість рядків з літерою 'z': {}".format(z_line_count))
        print("Кількість літер 'z' у файлі: {}".format(z_count))
        print("Кількість рядків з групою символів 'and': {}".format(and_line_count))

    # Питаємо користувача, чи хоче він проаналізувати ще один файл
    choice = input("Чи хочете ви проаналізувати ще один файл? (y/n): ")
    if choice.lower() != 'y':
        break
