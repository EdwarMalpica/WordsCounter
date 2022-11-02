import threading as th
import os
import time
import multiprocessing as multip

class jobs(multip.Process):

    def __init__(self, name, steps, interval=0.1):
        self._steps = steps
        self._interval = interval
        super().__init__(name=name)

    def run(self):
        for step in range(self._steps):
            print(f'Process ID: {os.getpid()} --> {self._name} and step: {step}')
            time.sleep(self._interval)


if __name__ == "__main__":
    job1 = jobs(name='Task 1:', steps=5)
    job2 = jobs(name='Task 2:', steps=5)
    job1.start()
    time.sleep(0.1)
    job2.start()