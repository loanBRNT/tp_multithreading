from Manager.py import QueueClient


class Minion:
    def __init__(self):
        self.tache = None
        self.queue = QueueClient()
        self.result = None

    def takeATask(self, t):
        self.tache = t

    def lookForATask(self):
        if self.queue.taskAvailaible():
            self.takeATask(self.queue.getATask())
            return True
        return False

    def taskEnded(self):
        self.queue.taskEnded(self.result)
        self.tache = None

    def workOnTask(self):
        self.tache.work()
        self.result = self.tache.x
