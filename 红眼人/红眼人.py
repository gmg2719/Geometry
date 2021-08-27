import numpy as np


class Person:
    def __init__(self):
        pass

    def handle(self, msg):
        pass


a = [Person() for i in range(10)]
b = np.random.randint(0, 2, len(a))


def broadcast(msg: str):
    # 广播一条消息
    msg_list = [msg]
    for i in a:
        if i.handle(msg):
            pass


for i in a:
    for ind, j in enumerate(a):
        if i == j:
            continue
        i.handle(f"{j.name} is {b[ind]}")

broadcast(f"has {0}")
