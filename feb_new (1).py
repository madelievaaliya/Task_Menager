import json
from datetime import datetime

class Task:
    def __init__(self, text):
        self.text = text
        self.done = False
        self.created_at = datetime.now().strftime("%d.%m.%Y %H:%M")
        
    def complete(self):
        self.done = True
    
    def to_dict(self):
        return {
            "text": self.text,
            "done": self.done,
            "created_at": self.created_at
        }  

    
class TaskManager:
    def __init__(self):
        self.tasks = []  
        
    def add_task(self, text):
        task = Task(text)
        self.tasks.append(task)
        
    def get_tasks(self):
        return self.tasks
        
    def task_done_change(self, index):        
        task = self.tasks[index]
        task.complete()        

    def task_edit(self, index, new_text):        
        task = self.tasks[index]
        task.text = new_text

    def delete_task(self, index):
        del self.tasks[index]
        
    def task_search(self, text):
        return  [task for task in self.tasks if text.lower() in task.text.lower()]
        # for item in self.tasks:
        #     if text.lower() in item.text.lower():
        #         empty.append(item.text)
            

    def get_statistic(self):
        total = len(self.tasks)
        count_done = len([task for task in self.tasks if task.done])
        # for task in self.tasks:
        #     if task.done:
        #         count_done += 1
        count_not_done = total - count_done
        return total, count_done, count_not_done
    
    def get_sorted_by_status(self):
        sorted_list = sorted(self.tasks, key=lambda task: task.done)
        # for task in self.tasks:
        #     if not task.done:
        #         sorted_list.append(task)
        # for task in self.tasks:
        #     if task.done:
        #         sorted_list.append(task) 
        return sorted_list   
    
    def get_sorted_by_date(self):  
        sorted_list = sorted(self.tasks, key=lambda task: task.created_at)
        # for task in self.tasks:
        #     for i,task2 in enumerate(sorted_list):
        #         if task.created_at <= task2.created_at:
        #             sorted_list.insert(i,task)
        #             break
        #     else:
        #         sorted_list.append(task)   
        return sorted_list   
        

    def save_to_file(self):
        data = [task.to_dict() for task in self.tasks]
        # for task in self.tasks:
        #     di = task.to_dict()
        #     data.append(di)
        with open('tasks.json', 'w', encoding='utf-8') as file:
            json.dump(data, file,ensure_ascii=False, indent=4)
            
    def load_from_file(self):
        #self.tasks = [задача1, задача2, задача3]
        self.tasks = []
        #self.tasks = []
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file: #tasks.json = [задача1, задача2]
                data = json.load(file)
                for item in data:
                    task = Task(item['text'])
                    task.done = item['done']
                    # if 'created_at' in item:
                    #     task.created_at = item['created_at']
                    # print(task.created_at)
                    task.created_at = item.get("created_at", task.created_at)
                    self.tasks.append(task) 
                #self.tasks = [задача1, задача2]        
        except FileNotFoundError:
            pass      
        
        
taskmanager = TaskManager()
taskmanager.load_from_file()  
   

def valid_input(index):
    result = index >= 0 and index < len(taskmanager.tasks)

    return result

def show_tasks(st = True):
    for i,task in enumerate(taskmanager.get_tasks()):
        if not task.done or st:
            status = '+' if task.done else '-' 
            print(f'{i}: {task.text} : {task.created_at} : ({status})')

while True:
    print('1 - Показать задачи')  
    print('2 - Добавить задачу')  
    print('3 - Отметить задачу выполненной') 
    print('4 - Удалить задачу')
    print('5 - Редактировать задачу')
    print('6 - Показать только НЕВЫПОЛНЕННЫЕ задачи')  
    print('7 - Поиск задачу по ключевому слову')   
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
        taskmanager.add_task(new_add_task)
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
    
    
    
    
    
               
                            
            









  