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
    except FileExistsError:
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
            pass  # Попросить ввести номер задачи для отметки выполнения. Проверить есть ли такая задача.
        elif command == 'delete':
            pass  # Удалить задачу
        elif command == 'exit':
            print("Выход...")
            break
        else:
            print("Неизвестная команда. Попробуйте ещё раз.")

main()
