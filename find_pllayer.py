import tkinter as tk

# Создаем словари с данными игроков для двух команд
team_a = {
    10: ("Бухаров", "Владислав"),
    55: ("Мельник", "Даниил"),
    90: ("Антонов", "Егор"),
    9: ("Белов", "Евгений"),
    96: ("Назаров", "Олег"),
    17: ("Морозов", "Денис"),
    52: ("Родионов", "Денис"),
    23: ("Трапезников", "Александр"),
    11: ("Соколов", "Макар"),
    42: ("Гришаев", "Никита"),
    93: ("Ивачев", "Николай"),
    99: ("Новиков", "Игорь"),
    98: ("Авксентьев", "Александр"),
    4: ("Охальский", "Иван"),
    95: ("Медведев", "Дмитрий"),
    15: ("Бабкин", "Артем"),
    65: ("Соколов", "Андрей"),
    92: ("Басов", "Дмитрий")

}

team_b = {
    11: ("Колчин", "Егор"),
    13: ("Алешенков", "Дмитрий"),
    14: ("Язев", "Михаил"),
    19: ("Назаренко", "Дмитрий"),
    21: ("Жидков", "Павел"),
    52: ("Игошин", "Константин"),
    55: ("Петрушин", "Артем"),
    69: ("Петров", "Даниил"),
    71: ("Мандриков", "Роман"),
    72: ("Корольков", "Никита"),
    77: ("Савельев", "Владислав"),
    88: ("Леонов", "Лев"),
    91: ("Ларионов", "Павел"),
    95: ("Васильев", "Никита"),
    96: ("Колоыркин", "Артем"),
    98: ("Овчинников", "Семен")
}

def lookup_players(event=None):
    # Получаем номер игрока из выбранной строки (строка А или Б)
    numbers = entry_field.get().split(',')
    results = []

    # Проверяем, есть ли в списке numbers хотя бы один элемент
    if numbers:
        # Проверяем номера для выбранной команды
        for number in numbers:
            number = int(number.strip())
            # Проверяем, не равен ли номер 0
            if number != 0:
                if chosen_team.get() == 'A':
                    if number in team_a:
                        last_name, first_name = team_a[number]
                        results.append(f"Запад России: {first_name} {last_name} - {number}") # Изменили порядок вывода
                    else:
                        results.append(f"Запад России: Игрок с номером {number} не найден.")
                elif chosen_team.get() == 'B':
                    if number in team_b:
                        last_name, first_name = team_b[number]
                        results.append(f"Соперник: {first_name} {last_name} - {number}") # Изменили порядок вывода
                    else:
                        results.append(f"Соперник: Игрок с номером {number} не найден.")
    else:
        results.append("Пожалуйста, введите хотя бы один номер.")

    # Обновляем метку с результатами
    result_label.config(text="\n".join(results))

def clear_output(event=None):
    result_label.config(text="")

# Создаем основное окно
root = tk.Tk()
root.title("Поиск Игроков")
root.geometry("500x400") # Увеличиваем размеры окна

# Создаем метки и поля ввода для номеров игроков
team_a_label = tk.Label(root, text="Номера игроков:")
team_a_label.pack(pady=10)
entry_field = tk.Entry(root) # Используем одно поле ввода
entry_field.pack(pady=10)
entry_field.bind('<Return>', lookup_players) # Добавляем обработчик события <Return>

# Создаем кнопку для поиска игроков
lookup_button = tk.Button(root, text="Найти игроков", command=lookup_players)
lookup_button.pack(pady=10)

# Создаем метку для отображения результата
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Переменная, которая будет хранить выбранную команду
chosen_team = tk.StringVar(value='A')

# Создаем радиокнопки для выбора команды
radio_button_a = tk.Radiobutton(root, text="Запад России", variable=chosen_team, value='A', command=lookup_players)
radio_button_a.pack(pady=10)
radio_button_b = tk.Radiobutton(root, text="Соперник", variable=chosen_team, value='B', command=lookup_players)
radio_button_b.pack(pady=10)

# Добавляем обработчик события для очистки вывода
entry_field.bind('<0>', clear_output)

# Запускаем главный цикл GUI
root.mainloop()


