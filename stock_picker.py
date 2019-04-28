import csv
import sys
import math
from datetime import datetime

from stock_search import StockSearch


class Interval(object):
    def __init__(self):

        self.buy = 0
        self.sell = 0
        self.profit = 0
        self.b_date = ""
        self.s_date = ""


def read_csv_file(filename):

    rows = []
    with open(filename, "r") as csvfile:

        csvreader = csv.reader(csvfile)
        for row in csvreader:
            date_ = datetime.strptime(row[1], "%d-%b-%Y")
            row[1] = date_.date()
            row[2] = float(row[2])
            rows.append(row)
    return rows


if __name__ == "__main__":

    filename = sys.argv[1]
    stock_search = StockSearch()

    rows = []
    rows = read_csv_file(filename)
    for row in rows:
        stock_search.insert(row[0])

    while rows:

        name = input("Welcome Agent! Which stock you need to process? ")
        print(stock_search.search(name))
        status, name = stock_search.search(name)

        if not status:
            resp = input("Oops! Do you mean {0}? y or n : ".format(name))

            if resp != "y":
                continue

        sdate = input("From which date you want to start : ")
        ldate = input("Till which date you want to analyze : ")
        sdate = datetime.strptime(sdate, "%d-%b-%Y").date()
        ldate = datetime.strptime(ldate, "%d-%b-%Y").date()
        amt = 0
        mean = 0
        sd = 0.0
        values = []

        for row in rows:
            if row[0] == name and row[1] >= sdate and row[1] <= ldate:
                each = [0] * 2
                each[0] = row[1]
                each[1] = row[2]
                values.append(each)

        if not len(values):
            print(
                "No data available for stock {0} between {1} and {2}".format(
                    name, sdate.strftime("%d-%b-%Y"), ldate.strftime("%d-%b-%Y")
                )
            )
            continue

        n = len(values)

        for i in range(n):

            for j in range(n - i - 1):

                if values[j][0] > values[j + 1][0]:
                    values[j], values[j + 1] = values[j + 1], values[j]

        for each in values:

            amt += float(each[1])

        mean = amt / n

        for row in values:
            sd += (row[1] - mean) ** 2

        sd = math.sqrt(sd / n)
        sol = []
        i = 0

        while i < n - 1:

            while i < n - 1 and values[i + 1][1] <= values[i][1]:
                i += 1

            if i == n - 1:
                break

            interval = Interval()

            interval.b_date = values[i][0]
            interval.buy = float(values[i][1])
            i += 1

            while i < n and values[i][1] >= values[i - 1][1]:
                i += 1
            if i == n - 1:
                break

            interval.s_date = values[i - 1][0]
            interval.sell = float(values[i - 1][1])
            interval.profit = (interval.sell - interval.buy) * 100

            sol.append(interval)

        if not len(sol):
            print("Stock cannot be sold in given period to have profit")
            continue

        max_ = sol[0].profit
        index = 0

        for i in range(len(sol) - 1):

            if max_ < sol[i].profit:
                max_ = sol[i].profit
                index = i

        print(
            "Here is you result : Mean = {0} , Std = {1} , Buy Date = {2} , Sell Date = {3} , Profit = {4}".format(
                mean,
                sd,
                sol[index].b_date.strftime("%d-%b-%Y"),
                sol[index].s_date.strftime("%d-%b-%Y"),
                sol[index].profit,
            )
        )

        x = input("Do you want to continue? (Y or N) : ")

        if x == "n" or x == "N":
            exit()

        else:
            continue
