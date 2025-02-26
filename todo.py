def display_menu():
    print('\n Menu: ')
    print('1. Add task')
    print('2. View tasks')
    print('3. Mark as done')
    print('4. Exit')


def add_task(tasks):
    task = str(input("Please input task description: "))
    tasks.append(task)
    print('Task Added Successfully')


def view_tasks(tasks):
    print('\n Tasks:')
    [print(f"{index}. {x}") for index, x in enumerate(tasks)]


def tasks_mark_done(tasks):
    if not tasks:
        print("No tasks to mark as done.")
        return

    view_tasks(tasks)
    index = int(input("Enter task index to mark as done: "))

    try:
        print(f"Item at index {index}: {tasks[index]}")
        removed_tasks = tasks.pop(index)
        print(f"{removed_tasks} has been removed and marked as done.")
    except IndexError:
        print("Index out of range or Invalid index.")


def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + '\n')


def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


def main():

    tasks = load_tasks()

    while True:
        display_menu()

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            tasks_mark_done(tasks)
        elif choice == '4':
            print("Exiting...")
            save_tasks(tasks)
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
