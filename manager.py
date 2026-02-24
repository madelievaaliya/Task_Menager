import json
from models import Task

class TaskManager:
    def __init__(self):
        self.tasks = []  
        
    def add_task(self, text, priority):
        task = Task(text, priority)
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
                    task.priority = item.get("priority", "Medium")
                    task.done = item['done']
                    # if 'created_at' in item:
                    #     task.created_at = item['created_at']
                    # print(task.created_at)
                    task.created_at = item.get("created_at", task.created_at)
                    self.tasks.append(task) 
                #self.tasks = [задача1, задача2]        
        except FileNotFoundError:
            pass      