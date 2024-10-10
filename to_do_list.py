# Путь к файлу
file_path = "README.md"

def add_task(task):
    with open(file_path, "a") as file:
        file.write(f"- [ ] {task}\n")
    print(f"Задача '{task}' добавлена в README.md")


def show_task():
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
            if not content:
                print("Список задач пуст.")
            else:
                print("Список задач:")
                for line in content:
                    print(line.strip())
    except FileNotFoundError:
        print("Файл README.md не найден.")


def complete_task(task_number):  # fail
    try:
        with open(file_path, "r") as file:
            content = file.readlines()
        if 0 < task_number <= len(content):
            content[task_number - 1] = content[task_number - 1].replace("[ ]", "[x]")

            with open(file_path, "w") as file:
                content = file.writelines()
            print(f"Задача {task_number} отмечена как выполненная.")
        else:
            print("Задача с таким номером не найдена.")
    except FileNotFoundError:
        print("Файл README.md не найден.")


def main():
    while True:
        command = input("Введите команду (add/show/complete/delete/exit): ")

        if command == 'add':
            task = input("Введите задачу: ")
            add_task(task)
        elif command == 'show':
            show_task()
        elif command == 'complete':
            task_number = int(input("Введите номер задачи: "))
            complete_task(task_number)
        elif command == 'delete':
            pass  # Удалить задачу
        elif command == 'exit':
            print("Выход...")
            break
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

main()
