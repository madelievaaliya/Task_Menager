from datetime import datetime

class Task:
    def __init__(self, text, priority="Medium"):
        self.text = text
        self.done = False
        self.priority = priority
        self.created_at = datetime.now().strftime("%d.%m.%Y %H:%M")
        
    def complete(self):
        self.done = True
    
    def to_dict(self):
        return {
            "text": self.text,
            "done": self.done,
            "priority": self.priority,
            "created_at": self.created_at
        }  
