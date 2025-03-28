"""
Write a program for creating a todo list using ‘Lists-Data Structure’ in Python
The program should have the functions to display the tasks, add a task, and
remove a task. Use functions wherever applicable so as make code appear more
modular in nature. (Add search function as well as an additional feature in
order to search for the tasks in the todo list using key words). You are
expected to use conditional statements, looping constructs wherever applicable.
"""

from pathlib import Path
from json import loads, dumps

TODO: list[str] = []


def add_task(task: str) -> bool:
    return not (TODO.append(task) if task else True)


def remove_task() -> bool:
    if not len(TODO):
        return False
    display_tasks()    
    print()
    to_rm = int(input("Enter task to remove: ")) - 1
    if not (0 <= to_rm < len(TODO)):
        return False
    else:
        TODO.pop(to_rm)
        return True
    

def search_task(keyword: str):
    for task in TODO:
        if keyword in task:
            yield task


def display_tasks() -> None:
    for idx, task in enumerate(TODO, 1):
        print(f"{idx}. {task}")


def menu(save_fl: Path) -> None:
    prompt: str = (
"""
1. Add task
2. Remove task
3. Show tasks
4. Search tasks
5. Exit

Enter choice: 
"""
        ).strip('\n')
    
    while True:
        choice: int = int(input(prompt))

        if not (1 <= choice <= 5):
            print("Invalid choice!")
        elif choice == 1:
            if not add_task(input("Enter task to add to TODO list: ")):
                print("Empty tasks don't count")
        elif choice == 2:
            if remove_task():
                print("Could not remove task!")
        elif choice == 3:
            display_tasks()
        elif choice == 4:
            for task in search_task(input("Enter search term: ")):
                print(f"{task}")
        else:
            open(save_fl, "w").close()
            save_fl.write_text(dumps(TODO, indent=2))
            TODO.clear()
            return
        
        print("\n\n\n")


    
if __name__ == "__main__":
    save_fl: Path = Path(__file__).parent / "tasks.json"
    if save_fl.exists():
        TODO = loads(save_fl.read_text())
    menu(save_fl)