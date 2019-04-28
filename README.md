# EndGameAnalytics

## Problem Statement

A company named EndGameAnalytics needs to provide a tool all their agent to help
them calculate stock analytics. The fun part is all the company agents are developer
so they are well versed with command line tools.
You have to create a command line tool which will take user inputs like start_date,
end_date and stock_code(all alphabets) and display following metrics:
Mean value of the stock between the dates
Standard Deviation of the stock between the dates
On what date should the agent buy and and on what date he/she should sell the
stocks to gain maximum profit. He is only allowed to buy and sell once in between
the selected dates.
Profit achieved by buying and selling on the dates calculated above. (Assume he
buys 100 units of stocks)

To make it better we have to help the agent to make selection faster. To do that let’s
say he inputs stock_code as “AICIX” but there is not match but there is a very close
match with the name “AICIXE” then prompt the user “Do you mean AICIXE  (y/n)?”

CSV format
StockName StockDate StockPrice

AICIXE 20-Jan-2019 20.453

AMBKP 20-Jan-2019 30.500

AICIXE 21-Jan-2019 21.000

AMBKP 22-Jan-2019 29.321

AMBKP 24-Jan-2019 35.453

**To be noted:**
CSV records can have any order and dates can be any order.
In case of missing date use the previous day stock price.
keep in mind the code never crashes and all edge cases are handled properly.
Do not use pandas and numpy. You can make the output better by adding your extra communication for hand
holding agents , showing loaders, adding support for all date formats, etc, etc. Go
innovative.
Test cases are added points.

## Running the CLI (Tested on Python 3.5.2)

```sh
python3 stock_picker.py “pathtocsv”
```

## Running the tests (Tested on Python 3.5.2)

```sh
python3 tests.py
```

