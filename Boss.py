from Manager import QueueClient
from Task import Task

NB_TASK = 10


class Boss(QueueClient):
    def __init__(self):
        self.queue = QueueClient()

    def createTask(self, task):
        print("Created task : " + str(task.identifier))
        self.queue.tasks.put(task)


if __name__ == "__main__":
    b = Boss()
    for i in range(NB_TASK):
        t = Task("T" + str(i))
        b.createTask(t)
