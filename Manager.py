class QueueManager:
    def __init__(self):
        self.task_queue = []
        self.result_queue = []

    def getTaskQueue(self):
        return self.task_queue

    def getResultQueue(self):
        return self.result_queue

    def getATask(self):
        temp = None
        if len(self.task_queue) > 0:
            temp = self.task_queue[0]
            self.task_queue.remove(0)
        return temp

    def addResult(self, result):
        self.result_queue.append(result)

    def addTask(self, task):
        self.task_queue.append(task)


class QueueClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(QueueClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.manager = QueueManager()

    def taskAvailaible(self):
        queue = self.manager.getTaskQueue
        if len(queue) == 0:
            return False
        return True

    def getATask(self):
        return self.manager.getATask()

    def taskEnded(self, result):
        self.manager.addResult(result)

    def createTask(self, task):
        self.manager.addTask(task)


if __name__ == "__main__":
    queue = QueueClient()
