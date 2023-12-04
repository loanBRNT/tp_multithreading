import json
import time

import numpy as np


class Task:
    def __init__(self, identifier, size=None, a=None, b=None):
        self.identifier = identifier
        # choosee the size of the problem
        self.size = size or np.random.randint(300, 3_000)

        # Generate the input of the problem
        if a is None:
            self.a = np.random.rand(self.size, self.size)
        else:
            self.a = a

        if b is None:
            self.b = np.random.rand(self.size)
        else:
            self.b = b

        # prepare room for the results
        self.x = np.zeros((self.size))
        self.time = 0

    def work(self):
        start = time.perf_counter()
        self.x = np.linalg.solve(self.a, self.b)
        self.time = time.perf_counter() - start

    def toJson(self):
        return json.dumps(
            {
                "a": self.a.tolist(),
                "b": self.b.tolist(),
                "s": self.size,
                "id": self.identifier,
            }
        )

    @classmethod
    def from_json(cls, s):
        dic = json.loads(s)
        return Task(
            dic["id"], size=dic["s"], a=np.array(dic["a"]), b=np.array(dic["b"])
        )

    def __eq__(self, t):
        if isinstance(t, Task):
            if np.array_equal(self.a, t.a) and np.array_equal(self.b, t.b):
                return True
        return False


if __name__ == "__main__":
    print("test unitaire a==b (True)")
    a = Task("000")
    txt = a.toJson()
    b = Task.from_json(txt)
    print(a == b)
    print("test unitaire a==c (False)")
    c = Task("001")
    print(a == c)
