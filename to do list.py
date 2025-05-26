import json
list=[]

def load_task():
    try:
        with open("list.json",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def save_task():
    with open('list.json','w') as file:
        json.dump(list, file)

def add_task():
    task=input('Enter the Task: ')
    list.append({'task':task,'done':False})
    save_task()
    print("Task was Added")

def show_task():
    if not list:
        print("No Tasks are Found")
    for i,value in enumerate(list):
        if value['done']:
            status='finished'
        else:
            status='unfinish'
        print(f"{i+1}. {value['task']} -- {status}")

def mark_task():
    index=int(input('Enter the Task numbere to Mark: '))
    if 0<index and index<=len(list):
        list[index-1]['done']=True
        save_task()
        print(f"The Task {index} was marked")
    else:
        print("Sorry you entered wrong Task number, Try Again")

def remove_task():
    index=int(input('Enter the Task numbere to remove: '))
    if 0<index and index<=len(list):
        list.pop(index-1)
        save_task()
        print(f"The Task {index} was removed from List ")
    else:
        print("Sorry you have enter incorrect task number, Try Again ")

def delete_all():
    list.clear() 
    save_task()   
    print("Deleted All Tasks ")    

def exit():
    print("--EXIT--")

def main():
    print("1. Add Task ")
    print("2. Check Task ")
    print("3. Mark as Done ")
    print("4. Delete Task ")
    print('5. Delete all tasks')
    print("6. Exit ")
list=load_task()

while True:
    main()
    choose=input("Enter the Option Number(1-6): ")

    if choose=='1':
        add_task()
    elif choose=='2':
        show_task()
    elif choose=='3':
        mark_task()
    elif choose=='4':
        remove_task()
    elif choose=='5':
        delete_all()
    elif choose=='6':
        exit()
        break
    else:
        print("Please Enter Correct option")