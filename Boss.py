from Manager import QueueClient
from Task.py import Task


class Boss(QueueClient):
    def __init__(self):
        self.queue = QueueClient()

    def createTask(self, task):
        self.queue.addTask(task)


if __name__ == "__main__":
    b = Boss()
    t = Task("000")
    b.createTask()
