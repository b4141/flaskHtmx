from random import randint
import datetime
from data import *

def random_date(start, end):
    return datetime.date(randint(start, end), randint(1, 12), randint(1, 28))

def generateData(customers, transactions):
    for i in range(len(customers)):
        transactions.append({"customer": customers[randint(0, len(customers)-1)], "amount": randint(20, 50),"date": random_date(2019, 2024)})


def getWorkingTimes():
    working_times = {}
    for i in range(9):
        noonTime = "AM"
        time = i+8
        if time >= 12:
            noonTime = "PM"
        if time < 10:
            time = f"0{time}"
        working_times[f"{time}:00 {noonTime}"] = None
        working_times[f"{time}:20 {noonTime}"] = None
        working_times[f"{time}:40 {noonTime}"] = None
    return working_times

def getTasksByDate(date):
    date = date.strftime('%Y-%m-%d')
    tasks = getWorkingTimes()
    for task in all_tasks:
        if all_tasks[task]["date"] == date:
            # pass
            tasks[all_tasks[task]["time"]] = {
                "costumer": all_tasks[task]["costumer"],
                "host": all_tasks[task]["host"],
                "task_id": task
            }
    return tasks
