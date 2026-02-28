

def valid_input(taskmanager, index):
    result = index >= 0 and index < len(taskmanager.tasks)

    return result

def show_tasks(taskmanager, st = True):
    for i,task in enumerate(taskmanager.get_tasks()):
        if not task.done or st:
            status = '+' if task.done else '-' 
            print(f'{i}: {task.text} | Priority: {task.priority} | {task.created_at} | ({status})')