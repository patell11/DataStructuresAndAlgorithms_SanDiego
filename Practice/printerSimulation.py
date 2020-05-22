from queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.remaining_time = 0
        self.printing_rate = ppm
        self.currentTask = None

    def tick(self):
        if self.remaining_time != None:
            self.remaining_time = self.remaining_time - 1
            if self.remaining_time <= 0:
                self.currentTask = None

    def isBusy(self):
        return self.currentTask

    def startNewTask(self, newtask):
        self.currentTask = newtask
        self.remaining_time = newtask.getPages() * (60 / self.printing_rate)

class Task:
    def __init__(self, time, pages):
        self.arrived_at = time
        self.no_of_pages = pages

    def getPages(self):
        return self.no_of_pages

    def waitingTime(self, current_time):
        return current_time - self.arrived_at


def simulation(seconds, pagesPerMinute):
    waiting_time = []
    tasks_queue = Queue()
    printer_operation = Printer(pagesPerMinute)

    for second in range(seconds):

        if newPrintTask():
            pages = random.randrange(1,20)
            new_task = Task(second,pages)
            tasks_queue.enqueue(new_task)

        if (not printer_operation.isBusy() and not tasks_queue.isEmpty()):
            task = tasks_queue.dequeue()
            printer_operation.startNewTask(task)

            waiting_time.append(task.waitingTime(second))

        printer_operation.tick()

    averageWait = sum(waiting_time) / len(waiting_time)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, tasks_queue.size()))

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)