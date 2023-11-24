import time

from Manager import QueueClient


class Minion:
    def __init__(self):
        self.tache = None
        self.queue = QueueClient()
        self.result = None

    def takeATask(self, t):
        self.tache = t

    def lookForATask(self):
        queue = self.queue.getTask()
        task = queue.get()
        if task:
            self.takeATask(task)
            return True
        return False

    def taskEnded(self):
        if self.result is not None:
            results = self.queue.getResult()
            results.put(self.result)
            self.tache = None
            self.result = None

    def workOnTask(self):
        print("Start working on :", self.tache.identifier)
        self.tache.work()
        self.result = self.tache.x


if __name__ == "__main__":
    minion = Minion()
    while 1:
        time.sleep(2)
        if minion.lookForATask():
            minion.workOnTask()
            minion.taskEnded()
