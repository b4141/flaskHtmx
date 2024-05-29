from flask import Flask, url_for, render_template, redirect
from random import randint
import datetime

app = Flask(__name__)


class Customer:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(self.name)

customers = []
listOfNames = ["Delilah Osborne", "Augustus Wilkins", "Amalia Harris", "Samuel Herring", "Denver Rasmussen", "Will Huynh", "Oaklee Fitzgerald", "Peyton Bates", "Madilyn Jimenez", "Silas Burgess", "Emory Wade", "Jake Savage", "Louise Lynch", "Zane Saunders", "Meadow Meyers", "Julien Pacheco", "Paris Gordon", "Karter Wolfe", "Hallie Magana", "Rey Daniel", "Joy Holt", "Niko Allison", "Chelsea Flynn", "Kannon Parrish", "Tiana Tyler", "Emmitt Hansen", "Hope Hammond", "Francis Jenkins", "Rylee Caldwell", "Rylan Barr", "Noemi Berger", "Byron Trujillo", "Danielle Best", "Harlem Sosa", "Cassandra Long", "Jace Parrish", "Tiana Evans"]

for i in range(len(listOfNames)):
    customers.append(Customer(listOfNames[i]))

class Transaction:
    def __init__(self, customer, amount, date):
        self.customer =  customer
        self.amount = amount
        self.date = date

transactions = []

def random_date(start, end):
    return datetime.date(randint(start, end), randint(1, 12), randint(1, 28))

for i in range(100):
    transactions.append(Transaction(customers[randint(0, len(customers)-1)], randint(20, 50),random_date(2019, 2024)))


@app.route("/")
def index():
    print(transactions[0].customer.name)
    return render_template("index.html", title="index")

@app.route("/transactions")
def transactionsRoute():
    print(transactions[0].customer.name)
    return render_template("transactions.html", title="transactions", transactions=transactions)

if __name__ == "__main__":
    app.run(debug=True)
