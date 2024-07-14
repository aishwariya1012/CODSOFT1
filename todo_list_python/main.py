def insert_task():
    n=int(input('How many tasks to enter:'))
    for i in range(n):
        task=input('Enter the task:')
        to_do.append({"task":task,"done":False})
    print('Insertion completed')

def remove_task():
    task=int(input('Enter the task number to remove:'))
    if task>0 and task<=len(to_do):
        to_do.pop(task-1)
        print('Task removed')
    else:
        print('Invalid input')

def display_task():
    if not to_do:
        print('List empty')
    else:
        for index,tasks in enumerate(to_do,1):
            d="Done" if tasks["done"] else "Not done"
            print(f"{index}. {tasks["task"]} - {d}")


def mark_task():
    n=int(input("Enter task to mark:"))
    if n>0 and n<=len(to_do):
        to_do[n-1]["done"] = True
        print("Marked as done")
    else:
        print('Invalid input')

to_do=[]
print('TO-DO LIST APP:')
print('--------------------------')
while True:
    print('MENU:')
    print('1.add a task\n'
          '2.remove a task\n'
          '3.mark as done\n'
          '4.display the to-do list\n'
          '5.exit\n')
    choice=int(input('Select any option:'))
    while choice:
        if choice==1:
            insert_task()
            break
        elif choice==2:
            remove_task()
            break
        elif choice==3:
            mark_task()
            break
        elif choice==4:
            display_task()
            break
        elif choice==5:
            break
        else:
            raise Exception('Invalid option entered')
    if choice==5:
        break





