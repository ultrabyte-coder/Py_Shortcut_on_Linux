# Developer: Aleksandr Kolesnikov

### Описание

Этот скрипт на Python создает ярлык для указанного файла Python (.py) на рабочем столе пользователя в среде Linux. Ярлык позволяет быстро запускать Python-скрипты с помощью двойного щелчка. Обратите внимание, что данный скрипт предназначен только для графических приложений.

### Установка

Для использования скрипта необходимо наличие установленного Python версии 3.11.

1. Скачайте или клонируйте репозиторий:

git clone https://github.com/ultranumb-coder/Py_Shortcut_on_Linux
cd Py_Shortcut_on_Linux

2. Убедитесь, что у вас установлен Python 3.11:

python3 --version

### Использование

1. Запустите скрипт:

Для запуска скрипта выполните команду в терминале:

python3 file_on_desktop_linux.py

2. Введите путь к файлу Python (.py):

После запуска вам будет предложено ввести полный путь к вашему Python-файлу. Например:

Введите путь к файлу Python (.py): /home/user/scripts/my_script.py

3. Проверьте рабочий стол:

На вашем рабочем столе должен появиться новый файл с расширением .desktop, который является ярлыком для вашего скрипта.

### Примечания

- Скрипт работает только в средах Linux и создает ярлыки в формате .desktop.
- Убедитесь, что указанный файл действительно существует и имеет расширение .py.
- Если указанный скрипт не является графическим приложением, он может не работать должным образом при запуске через созданный ярлык.
- Также проверьте права доступа к рабочему столу.
- Скрипт автоматически добавляет права на выполнение к созданному ярлыку.

### Ограничения

- Linux: Скрипт предназначен только для работы в системах, которые поддерживают .desktop файлы (например, Ubuntu, Fedora и другие дистрибутивы).
- Windows или macOS: Для других операционных систем потребуется другой подход. Например:
    - На Windows можно использовать .bat файлы или создавать ярлыки с помощью библиотек, таких как pywin32.
    - На macOS можно использовать AppleScript или Automator для создания ярлыков.

### Пример

Если вы хотите создать ярлык для скрипта my_script.py, находящегося по адресу /home/user/scripts/my_script.py, просто запустите скрипт и введите этот путь. 
Ярлык будет создан на вашем рабочем столе и позволит запускать его с помощью двойного щелчка.

### Лицензия

Этот скрипт является моим личным проектом. Я разрешаю всем пользователям пользоваться им безвозмездно.


# Developer: Aleksandr Kolesnikov

### Description

This Python script creates a shortcut for a specified Python file (.py) on the user's desktop in a Linux environment. The shortcut allows quick launching of Python scripts with a double-click. Note that this script is intended only for graphical applications.

### Installation

To use the script, you need to have Python version 3.11 installed.

1. Download or clone the repository:

git clone https://github.com/ultranumb-coder/Py_Shortcut_on_Linux
cd Py_Shortcut_on_Linux

2. Ensure that you have Python 3.11 installed:

python3 --version

### Usage

1. Run the script:

To run the script, execute the following command in the terminal:

python3 file_on_desktop_linux.py

2. Enter the path to the Python file (.py):

After launching, you will be prompted to enter the full path to your Python file. For example:

Enter the path to the Python file (.py): /home/user/scripts/my_script.py

3. Check your desktop:

A new file with the .desktop extension, which is a shortcut for your script, should appear on your desktop.

### Notes

- The script works only in Linux environments and creates shortcuts in the .desktop format.
- Ensure that the specified file exists and has a .py extension.
- If the specified script is not a graphical application, it may not work properly when launched through the created shortcut.
- Also, check the permissions for the desktop.
- The script automatically adds execution rights to the created shortcut.

### Limitations

- Linux: The script is designed to work in systems that support .desktop files (e.g., Ubuntu, Fedora, and other distributions).
- Windows or macOS: Other operating systems will require a different approach. For example:
    - On Windows, you can use .bat files or create shortcuts using libraries like pywin32.
    - On macOS, you can use AppleScript or Automator to create shortcuts.

### Example

If you want to create a shortcut for the script my_script.py located at /home/user/scripts/my_script.py, simply run the script and enter this path. 
The shortcut will be created on your desktop, allowing you to launch it with a double click.

### License

This script is my personal project. I allow all users to use it free of charge.