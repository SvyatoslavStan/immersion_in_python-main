class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        if item not in self.items:
            self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def __contains__(self, item):
        return item in self.items

    def __repr__(self):
        return "; ".join(self.items)


class TaskManager:
    def __init__(self):
        self.tasks = {}

    def new_task(self, task, priority):
        if priority not in self.tasks:
            self.tasks[priority] = Stack()
        self.tasks[priority].push(task)

    def remove_task(self, task):
        for priority in list(self.tasks.keys()):
            if task in self.tasks[priority]:
                self.tasks[priority].items.remove(task)
                if not self.tasks[priority].items:
                    del self.tasks[priority]

    def __str__(self):
        result = []
        for priority in sorted(self.tasks):
            result.append(f"{priority} — {self.tasks[priority]}")
        return "\n".join(result)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
manager.remove_task("сделать уборку")
print("\nПосле удаления задачи:")
print(manager)
