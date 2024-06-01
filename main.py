from flask import Flask, url_for, render_template, redirect, request
from random import randint
import datetime

app = Flask(__name__)


customers = [
    {"name": "Delilah Osborne"},
    {"name": "Augustus Wilkins"},
    {"name": "Amalia Harris"},
    {"name": "Samuel Herring"},
    {"name": "Denver Rasmussen"},
    {"name": "Will Huynh"},
    {"name": "Oaklee Fitzgerald"},
    {"name": "Peyton Bates"},
    {"name": "Madilyn Jimenez"},
    {"name": "Silas Burgess"},
    {"name": "Emory Wade"},
    {"name": "Jake Savage"},
    {"name": "Louise Lynch"},
    {"name": "Zane Saunders"},
    {"name": "Meadow Meyers"},
    {"name": "Julien Pacheco"},
    {"name": "Paris Gordon"},
    {"name": "Karter Wolfe"},
    {"name": "Hallie Magana"},
    {"name": "Rey Daniel"},
    {"name": "Joy Holt"},
    {"name": "Niko Allison"},
    {"name": "Chelsea Flynn"},
    {"name": "Kannon Parrish"},
    {"name": "Tiana Tyler"},
    {"name": "Emmitt Hansen"},
    {"name": "Hope Hammond"},
    {"name": "Francis Jenkins"},
    {"name": "Rylee Caldwell"},
    {"name": "Rylan Barr"},
    {"name": "Noemi Berger"},
    {"name": "Byron Trujillo"},
    {"name": "Danielle Best"},
    {"name": "Harlem Sosa"},
    {"name": "Cassandra Long"},
    {"name": "Jace Parrish"},
    {"name": "Tiana Evans"}
]

transactions = []

def random_date(start, end):
    return datetime.date(randint(start, end), randint(1, 12), randint(1, 28))

for i in range(100):
    transactions.append({"customer": customers[randint(0, len(customers)-1)], "amount": randint(20, 50),"date": random_date(2019, 2024)})

@app.route("/")
def index():
    # print(transactions[0].customer.name)
    return render_template("index.jinja", title="index")

@app.route("/transactions", methods=['GET', 'POST'])
def transactionsRoute():
    if request.method == 'POST':
        sort_by = request.form.get('sort_by')
        print("*****", sort_by)
        return render_template("transactionsRoute/transactionsTable.jinja", transactions=transactions[:10], sortedBy={"value":"name", "ascending":True})
    return render_template("transactionsRoute/transactions.jinja", title="transactions", transactions=transactions, sortedBy={"value": None})

if __name__ == "__main__":
    app.run(debug=True)
