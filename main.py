from manager import TaskManager


taskmanager = TaskManager()
taskmanager.load_from_file()  
   

def valid_input(index):
    result = index >= 0 and index < len(taskmanager.tasks)

    return result

def show_tasks(st = True):
    for i,task in enumerate(taskmanager.get_tasks()):
        if not task.done or st:
            status = '+' if task.done else '-' 
            print(f'{i}: {task.text} | Priority: {task.priority} | {task.created_at} | ({status})')

while True:
    print('1 - Показать задачи')  
    print('2 - Добавить задачу')  
    print('3 - Отметить задачу выполненной') 
    print('4 - Удалить задачу')
    print('5 - Редактировать задачу')
    print('6 - Показать только НЕВЫПОЛНЕННЫЕ задачи')  
    print('7 - Поиск 1')   
    print('8 - Сохранить задачи')
    print('9 - Показать статистику') 
    print('10 - Показать список задач по статусу') 
    print('11 - Показать отсортированный список по дате')
    print('12 - Показать отсортированный список по дате')
    print('0 - Выйти') 
    
    choice = input('Выбор: ')
    
    if choice == '1':
        if not taskmanager.tasks:
            print('Список задач пока пустой...')
        else:
            show_tasks()

                
    elif choice == '2':
        new_add_task = input('Введите новую задачу: ')
        
        print("Выберите приоритет:")
        print("1 - High")
        print("2 - Medium")
        print("3 - Low")
        
        priority_choice = input("Ваш выбор: ")
        
        if priority_choice == "1":
            priority = "High"
        if priority_choice == "2":
            priority = "Medium" 
        if priority_choice == "3":
            priority = "low"         
            
        taskmanager.add_task(new_add_task, priority)
        taskmanager.save_to_file()
        print('Новая задача добавлена!')
                    
    elif choice == '3':
        show_tasks(False)
        try:
            index = int(input('Введите номер задачи: ')) 
            if valid_input(index):
                taskmanager.task_done_change(index)
                taskmanager.save_to_file()
            else:
                print('Такой задачи нет либо не создан...')
            
        except ValueError:
            print('Вы ввели что то не то...')    

    elif choice == '4':  
        show_tasks()
        try:
            index = int(input('Введите номер задачи: ')) 
            if valid_input(index):
                isDelete = input("Вы уверены? (Да/Нет): ").strip()
                if isDelete.lower() == "да":
                    taskmanager.delete_task(index)
                    print("Задача удалена")
                else:
                    print("Список остался без изменений")
                taskmanager.save_to_file()
            else:
                print('Такой задачи нет либо не создан...')
            
        except ValueError:
            print('Вы ввели что то не то...')                     
              
    elif choice == '5':  
        show_tasks()
        try:
            index = int(input('Введите номер задачи: ')) 
            if valid_input(index):
                new_text = input("Введите новый текст: ").strip()
                taskmanager.task_edit(index, new_text)
                taskmanager.save_to_file()
            else:
                print('Такой задачи нет либо не создан...')
            
        except ValueError:
            print('Вы ввели что то не то...') 

    elif choice == '6':
        show_tasks(False)
    elif choice == '8':
        taskmanager.save_to_file()
        
    elif choice == "7":    
        new_text = input('Введите ключевое слово: ')
        tasks = taskmanager.task_search(new_text)
        for task in tasks:
            print(task.text)
        
    elif choice == '9':
        total, count_done, count_not_done = taskmanager.get_statistic()
        print("Количество задач:", total)
        print("Количество выплненых:", count_done)
        print("Количество невыплненых:", count_not_done)
        
    elif choice == '10': 
        sorted_tasks = taskmanager.get_sorted_by_status()
        for task in sorted_tasks:
            print(f"{task.text} : {'Выполнено' if task.done else 'Невыполнено'}")   
        
    elif choice == '11': 
        sorted_task_list = taskmanager.get_sorted_by_date()
        for task in sorted_task_list:
            print(f"{task.text} : {task.created_at}")
         
    elif choice == "0":
        taskmanager.save_to_file()
        break
    