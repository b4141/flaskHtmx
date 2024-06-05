from random import randint
import datetime
from utils import *

def random_date(start, end):
    return datetime.date(randint(start, end), randint(1, 12), randint(1, 28))

def generateData(customers, transactions):
    for i in range(len(customers)):
        transactions.append({"customer": customers[randint(0, len(customers)-1)], "amount": randint(20, 50),"date": random_date(2019, 2024)})

