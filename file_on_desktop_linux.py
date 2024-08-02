import os  # Импортируем модуль os для работы с операционной системой.
from pathlib import Path  # Импортируем класс Path из модуля pathlib для удобной работы с путями.


def create_shortcut(source_file):
    """
    Функция создает ярлык для указанного файла Python (.py) на рабочем столе пользователя.

    Parameters:
    source_file (str): Путь к исходному файлу Python, для которого будет создан ярлык.

    Returns:
    None: Функция не возвращает значение, но создает файл ярлыка на рабочем столе.
    """

    # Проверяем, что файл существует и является файлом Python (.py)
    if not os.path.isfile(source_file):
        print(f"Файл '{source_file}' не найден.")  # Сообщение об ошибке, если файл не существует.
        return

    if not source_file.endswith('.py'):
        print(f"Файл '{source_file}' не является файлом Python (.py).")  # Сообщение об ошибке, если файл не .py.
        return

    # Определяем путь к рабочему столу (Desktop)
    desktop_path = Path.home() / "Рабочий стол"  # Или "Desktop" на английском

    # Создаем ярлык (desktop entry)
    desktop_entry_file = desktop_path / (os.path.splitext(os.path.basename(source_file))[0] + '.desktop')
    # Формируем имя ярлыка из имени источника без расширения с добавлением .desktop.

    # Создаем .desktop файл
    with open(desktop_entry_file, 'w') as shortcut:
        shortcut.write("[Desktop Entry]\n")  # Начинаем запись стандартного заголовка .desktop файла.
        shortcut.write("Type=Application\n")   # Указываем тип записи - приложение.
        shortcut.write(f"Name={os.path.splitext(os.path.basename(source_file))[0]}\n")  # Имя приложения.
        shortcut.write(f"Exec=/usr/bin/python3 {source_file}\n")  # Команда для запуска файла с интерпретатором Python.
        shortcut.write("Icon=python\n")  # Иконка приложения.
        shortcut.write("Terminal=false\n")  # Указываем, что терминал не нужен для запуска.

    # Делаем .desktop файл исполняемым
    st = os.stat(desktop_entry_file)  # Получаем статус нового .desktop файла.
    os.chmod(desktop_entry_file, st.st_mode | 0o111)  # Добавляем права на выполнение к файлу.

    print(f"Ярлык для файла '{source_file}' создан на рабочем столе:\n{desktop_entry_file}")  # Подтверждение создания ярлыка.


if __name__ == "__main__":
    # Запрашиваем у пользователя путь к файлу .py
    py_file = input("Введите путь к файлу Python (.py): ").strip()  # Считываем ввод пользователя и убираем пробелы.

    # Создаем ярлык
    create_shortcut(py_file)  # Вызываем функцию для создания ярлыка с введенным путем к файлу.