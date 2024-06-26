from flask import Flask, url_for, render_template, redirect, request
from utils import *
from data import *
import json
import datetime
import calendar
import time

app = Flask(__name__)
generateData(customers, transactions)


@app.route("/")
def index():
    return render_template("index.jinja", title="index")


@app.route("/tasks")
def tasks():
    selected_date = datetime.datetime.today()
    days_in_month = calendar.monthrange(selected_date.year, selected_date.month)[1]
    days = []
    selected_week = selected_date.day // 8 if selected_date.day % 8 != 0 else selected_date.day / 8 - 1
    print(selected_week)
    for i in range(1, days_in_month+1, 8):
        week = []
        for j in range(i, min(i+8, days_in_month+1)):
            dayName = datetime.date(selected_date.year, selected_date.month, j).strftime("%a")
            dayNumber = f"0{j}" if j < 10 else str(j)
            week.append((dayNumber, dayName))
        days.append(week)
    selected_date = selected_date.strftime("%Y-%m-%d")
    working_times = []
    for i in range(9):
        noonTime = "AM"
        time = i+8
        if time >= 12:
            noonTime = "PM"
        if time < 10:
            time = f"0{time}"
        working_times.append(f"{time}:00 {noonTime}")
        working_times.append(f"{time}:20 {noonTime}")
        working_times.append(f"{time}:40 {noonTime}")
    args = {
        "date": selected_date,
        "days": days,
        "selected_week": selected_week+1,
        "working_times": working_times
    }
    return render_template("tasksRoute/tasks.jinja", title="Tasks", args=args)


@app.route("/transactions", methods=['GET', 'POST'])
def transactionsRoute():
    if request.method == 'POST':
        sort_by = request.form.get('sort_by')
        ascending = json.loads(request.form.get('ascending'))
        reverse_sort = True
        if ascending == True or ascending == False:
            reverse_sort = ascending
        if sort_by == "name":
            sorted_transactions = sorted(transactions, key=lambda x: x['customer']['name'], reverse=reverse_sort)
            return render_template("transactionsRoute/transactionsTable.jinja", transactions=sorted_transactions, sortedBy={"value":sort_by, "ascending":ascending})
        elif sort_by == "amount":
            sorted_transactions = sorted(transactions, key=lambda x: x["amount"], reverse=reverse_sort)
            return render_template("transactionsRoute/transactionsTable.jinja", transactions=sorted_transactions, sortedBy={"value":sort_by, "ascending":ascending})
        elif sort_by == "date":
            sorted_transactions = sorted(transactions, key=lambda x: x['date'], reverse=reverse_sort)
            return render_template("transactionsRoute/transactionsTable.jinja", transactions=sorted_transactions, sortedBy={"value":sort_by, "ascending":ascending})
    return render_template("transactionsRoute/transactions.jinja", title="transactions", transactions=transactions, sortedBy={"value": None, "ascending":True})


@app.route("/test", methods=['GET', 'POST'])
def test():
    date = datetime.datetime.strptime('2024-06-24', '%Y-%m-%d').date()
    args = {
        "working_times": getWorkingTimes(),
        "tasks": getTasksByDate(date),
    }
    return render_template("test.html", args=args)


@app.route("/test2", methods=['GET', 'POST'])
def test2():
    if request.method == 'POST':
        print(request.form.keys())
        # for key in request.form.keys():
        #     if times[key]:
        #         values = request.form.getlist(key)
        #         for value in values:
        #             if not value in times[key]:
        #                 print("ok")
        #                 times[key][value] = {"html_value": "hello 44"}
                        
        #             print(value)
        #     else:
        #         print("error: new time")
        # time.sleep(0.5)
        # return render_template("test2_form.html", times=times)
        # return "hello"
        # return render_template("test2_form.html", tasks=all_tasks)
        return
    return render_template("test2.html", tasks=all_tasks)


@app.route("/test3", methods=['GET', 'POST'])
def test3():
    date = datetime.datetime.strptime('2024-06-24', '%Y-%m-%d').date()
    args = {
        "working_times": getWorkingTimes(),
        "tasks": getTasksByDate(date),
    }
    return render_template("test3.html", args=args)

if __name__ == "__main__":
    app.run(debug=True)
