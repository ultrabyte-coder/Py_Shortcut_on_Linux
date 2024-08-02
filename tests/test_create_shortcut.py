import unittest
from unittest.mock import patch, mock_open
from pathlib import Path
from file_on_desktop_linux import create_shortcut


class TestCreateShortcut(unittest.TestCase):
    """Тестовый класс для проверки функции create_shortcut."""

    @patch('os.path.isfile')
    @patch('builtins.print')
    def test_file_not_found(self, mock_print, mock_isfile):
        """
        Тестирование случая, когда указанный файл не существует.

        Проверяет, что функция create_shortcut выводит сообщение об ошибке,
        если файл не найден. Для этого используется mock-объект, чтобы имитировать
        поведение функции os.path.isfile.

        Аргументы:
        - mock_print: Мок-объект для функции print.
        - mock_isfile: Мок-объект для функции os.path.isfile.
        """
        mock_isfile.return_value = False  # Файл не найден
        create_shortcut('non_existent_file.py')
        mock_print.assert_called_once_with("Файл 'non_existent_file.py' не найден.")

    @patch('os.path.isfile')
    @patch('builtins.print')
    def test_not_python_file(self, mock_print, mock_isfile):
        """
        Тестирование случая, когда указанный файл не является .py.

        Проверяет, что функция create_shortcut выводит сообщение о том, что
        файл не является файлом Python, если файл с указанным именем существует,
        но его расширение не .py.

        Аргументы:
        - mock_print: Мок-объект для функции print.
        - mock_isfile: Мок-объект для функции os.path.isfile.
        """
        mock_isfile.return_value = True  # Файл существует
        create_shortcut('not_a_python_file.txt')
        mock_print.assert_called_once_with("Файл 'not_a_python_file.txt' не является файлом Python (.py).")

    @patch('os.path.isfile')
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.chmod')
    @patch('os.stat')
    @patch('os.path.expanduser', return_value=str(Path.home()))
    @patch('os.path.join', side_effect=lambda *args: Path(*args))  # Для корректной обработки путей
    @patch('builtins.print')
    def test_create_shortcut_success(self, mock_print, mock_join, mock_expanduser, mock_stat, mock_chmod, mock_open, mock_isfile):
        """
        Тестирование успешного создания ярлыка на рабочем столе.

        Проверяет, что функция create_shortcut правильно создает .desktop файл,
        записывает нужные данные в него и устанавливает права доступа.

        Аргументы:
        - mock_print: Мок-объект для функции print.
        - mock_join: Мок-объект для функции os.path.join (используется для построения путей).
        - mock_expanduser: Мок-объект для функции os.path.expanduser.
        - mock_stat: Мок-объект для функции os.stat (для получения информации о файле).
        - mock_chmod: Мок-объект для функции os.chmod (для установки прав доступа).
        - mock_open: Мок-объект для функции open (для открытия файла).
        - mock_isfile: Мок-объект для функции os.path.isfile.
        """
        mock_isfile.return_value = True  # Файл существует
        source_file = '/path/to/script.py'
        mock_stat.return_value.st_mode = 0o755  # Пример режима файла

        create_shortcut(source_file)

        mock_open.assert_called_once_with(Path.home() / "Рабочий стол" / 'script.desktop', 'w')
        handle = mock_open()
        handle.write.assert_any_call("[Desktop Entry]\n")
        handle.write.assert_any_call("Type=Application\n")
        handle.write.assert_any_call(f"Name=script\n")
        handle.write.assert_any_call(f"Exec=/usr/bin/python3 {source_file}\n")
        handle.write.assert_any_call("Icon=python\n")
        handle.write.assert_any_call("Terminal=false\n")
        mock_chmod.assert_called_once()

        mock_print.assert_called_once_with(f"Ярлык для файла '{source_file}' создан на рабочем столе:\n{Path.home() / 'Рабочий стол' / 'script.desktop'}")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()

